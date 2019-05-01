import redis.clients.jedis.Jedis;

import java.util.List;

public class TestJedis {
    public static void main(String[] args){
        Jedis jedis = new Jedis("192.168.122.50");
        System.out.println("Connection to server successfully");
        jedis.lpush("tutorial-list","Redis");
        jedis.lpush("tutorial-list", "Mongodb");
        jedis.lpush("tutorial-list", "Mysql");

        List<String> list = jedis.lrange("tutorial-list", 0, 5);
        for(int i=0;i<list.size();i++){
            System.out.println("Stored string in redis::"+list.get(i));
        }

    }
}

