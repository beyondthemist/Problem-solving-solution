// https://euler.synap.co.kr/problem=9
// https://projecteuler.net/problem=9

public class Solution {
    
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        int a, b, c;
        int result = 0;
        
        for(a = 1; a <= 332; ++a) {
            for(b = a + 1; b <= 499; ++b) {
                c = 1000 - a - b;
                
                if(a*a + b*b == c*c) {
                    result = a*b*c;
                    return Integer.toString(result);
                }
            }
        }
        
        return Integer.toString(result);
    }
 
}
