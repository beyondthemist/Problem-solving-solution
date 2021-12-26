// https://euler.synap.co.kr/problem=5
// https://projecteuler.net/problem=5

import java.math.BigInteger;
import java.util.List;
import java.util.ArrayList;
 
public class Solution {
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        List<BigInteger> list = new ArrayList<BigInteger>(0);
        
        for(long i = 1L; i <= 20L; list.add(BigInteger.valueOf(i++)));
        
        return lcm(list.subList(1, list.size()), list.get(0)).toString();
    }
    
    public static BigInteger lcm(List<BigInteger> list, BigInteger b) {
        BigInteger val = (list.size() > 1) ? lcm(list.subList(1, list.size()), list.get(0))
                                           : list.get(0);
        
        return val.multiply(b).divide(val.gcd(b));
    }
}
