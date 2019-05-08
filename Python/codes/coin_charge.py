import unittest
"""
Recursive  time complexity:O(2*N)
"""
def coins_change(coin_values,money):
    min_count = money # Set money  as changed by 1 as default
    if money in coin_values: # Define the boundary 
        return 1             # The best situation is money equal to coin_values
    for value in [i for i in coin_values if i <=money]: # Iterating all the situation
        count = 1 + coins_change(coin_values,money-value) # f(n) = f(n-1) + 1
        if count < min_count:                             # if count lesser than last return
            min_count = count                             # Substitute count to min_count
    return min_count                                      # Return the  value

"""
Recursive using cache
memo algorithm : time complexity O(n),space complexity O(n)
@param: coins_values: a list of  denominations
        money : the money for change
        known_counts: a list using for cache result
"""
def coins_change_cache(coin_values,money,known_counts=None):
    if known_counts is None:
        known_counts = [ None for x in range(money + 1) ] # Why need plus 1? 
                                                          # Because 0 to money have money +1 
    min_count = money 
    if money in coin_values:
        return 1
    elif known_counts[money] is not None:
        return known_counts[money]
    for val in [ i for i in coin_values if i <= money]:
        count = 1 + coins_change_cache(coin_values,money-val,known_counts)
        if count < min_count:
            min_count = count
        known_counts[money] = min_count
    return min_count

"""
Dynamic Programing
"""
def coins_change_dp(coin_values,money,min_counts=None,last_used_coins=None):
    if min_counts is None:
        min_counts = [0 for x in range(money+1)]
    if last_used_coins is None:
        last_used_coins =  [0 for x in range(money+1)]
    for cent in range(money+1):
        min_count = cent
        for val in [ i for i  in coin_values if i <= cent]:
            if 1 + min_counts[cent - val] < min_count:
                min_count = 1 + min_counts[cent - val]
                last_used_coins[cent] = val
        min_counts[cent] = min_count

    # Print the used coins list
    used_coins = []
    while money > 0:
        used_coins.append(last_used_coins[money])
        money = money - last_used_coins[money]
    print(used_coins)
    return min_counts[-1]

class CoinChange(unittest.TestCase):
    def setUp(self):
        self.cv1 = [1,5,11]
        self.m1 = 15
        self.cv2 = [1,5,10,25]
        self.m2 = 63

    def test_coins_change(self):
        self.assertEqual(3,coins_change(self.cv1,self.m1))
        self.assertEqual(6,coins_change(self.cv2,self.m2))

    def test_coins_change_cache(self):
        self.assertEqual(3,coins_change_cache(self.cv1,self.m1))
        self.assertEqual(6,coins_change_cache(self.cv2,self.m2))

    def test_coins_change_dp(self):
        self.assertEqual(3,coins_change_dp(self.cv1,self.m1))
        self.assertEqual(6,coins_change_dp(self.cv2,self.m2))


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CoinChange('test_coins_change_cache'))
    suite.addTest(CoinChange('test_coins_change_dp'))
    unittest.TextTestRunner().run(suite)





