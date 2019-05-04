import threading
from threading import Lock

import unittest
import time

zero = 0
lock = Lock()
def change_zero_withlock():
    global zero
    for i in range(3000000):
        with lock:
            zero += 1
            zero -= 1

def change_zero_withoutlock():
    global zero
    for i in range(3000000):
        zero += 1
        zero -= 1


class TestThreadSafe(unittest.TestCase):

    def setUp(self):
        global zero
        zero = 0

    def tearDown(self):
        pass

    def test_without_lock(self):
        th1 = threading.Thread(target=change_zero_withoutlock)
        th2 = threading.Thread(target=change_zero_withoutlock)
        th1.start()
        th2.start()
        th1.join()
        th2.join()
        global zero
        var = zero
        print(var)
        self.assertNotEqual(var,0)

    def test_with_lock(self):
        th1 = threading.Thread(target=change_zero_withlock)
        th2 = threading.Thread(target=change_zero_withlock)
        th1.start()
        th2.start()
        th1.join()
        th2.join()
        global zero
        var = zero
        print(var)
        self.assertEqual(var,0)
        pass

if __name__ == '__main__':
    unittest.main()
