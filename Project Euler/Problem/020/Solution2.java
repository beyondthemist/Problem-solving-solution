// https//euler.synap.co.kr/problem=20
// https://projecteuler.net/problem=20

import java.math.BigInteger;
 
public class Solution2 {
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        BigInteger bi = BigInteger.ONE;
        int result = 0;
        
        for(int i = 1; i <= 100; i++) {
            bi = bi.multiply(new BigInteger(Integer.toString(i)));
        }
        
        while(!bi.equals(BigInteger.ZERO)) {
            result += bi.mod(BigInteger.TEN).intValue();
            bi = bi.divide(BigInteger.TEN);
        }
            
        return Integer.toString(result);
    }
}
