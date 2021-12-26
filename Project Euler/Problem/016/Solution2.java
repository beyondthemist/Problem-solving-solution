// https://euler.synap.co.kr/problem=16
//https://projecteuler.net/problem=16

import java.math.BigInteger;
 
// with java.math.BigInteger
public class Problem016 {
    private final static int N = 1000; 
 
    public static void main(String[] args) {
        System.out.println(run());
    }
 
    public static String run() {
        BigInteger num = new BigInteger("2");
        int result = 0;
        
        num = num.pow(N);
        
        while(!num.equals(BigInteger.ZERO)) {
            result += num.mod(BigInteger.TEN).intValue();
            num = num.divide(BigInteger.TEN);
        }
        
        return Integer.toString(result);
    }
 
}
