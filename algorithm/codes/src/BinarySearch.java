import java.util.Arrays;
import java.math.*;

public class BinarySearch{

    public static int rank(int key,int [] a){
        int lo=0;
        int hi=a.length-1;
        while (hi>=lo) {
            int mid=lo+(hi-lo)/2;
            if (a[mid] > key) {
                hi = mid-1;
            } else if (a[mid] < key) {
                lo = mid+1;
            } else {
                return mid;
            }
        }
        return -1;
    }



    public static void main(String [] args){
        int [] whitelist = In.readInts(args[0]);
        Arrays.sort(whitelist);
        System.out.print(Math.abs(-2147483648));
//        while (!StdIn.isEmpty()){
//            int key = StdIn.readInt();
//            if (rank(key, whitelist)<0){
//                StdOut.println(key);
//            }
//        }


    }
}