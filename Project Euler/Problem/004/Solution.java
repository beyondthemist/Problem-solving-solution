// https://euler.synap.co.kr/problem=4
// https://projecteuler.net/problem=4

public class Solution {
    public static void main(String args[]) {
      System.out.println(run()); 
    }
    
    public static String run() {
        int max = -1;
        
        for(int a = 111; a < 1000; a++) {
            for(int b = 111; b < 1000; b++) {
                int n = a*b;
                
                if((n > max) && isSymmetric(n)) {
                    max = n;
                }
            }
        }
        
        return Integer.toString(max);
    }
    
    public static boolean isSymmetric(int n) {
        String s = Integer.toString(n);
        int idx = s.length() / 2;
 
        while(idx > 0) {
            if(s.charAt(idx - 1) != s.charAt(s.length() - idx--)) return false;
        }
 
        return true;
    } 
}
