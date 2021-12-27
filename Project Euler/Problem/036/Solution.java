// https://euler.synap.co.kr/problem=36
// https://projecteuler.net/problem=36

public class Solutionj {
    public static void main(String args[]) {
      System.out.println(run());
    }
    
    public static String run() {
        int n = 1000000;
        int count = 0;
        
        do {
            if(isSymmetric(Integer.toString(n))
            && isSymmetric(Integer.toBinaryString(n))) {
                count += n;
            }
        } while(n-- > 0);
        
        return Integer.toString(count);
    }
    
    public static boolean isSymmetric(String s) {
        int idx = s.length() / 2;
 
        while(idx > 0) {
            if(s.charAt(idx - 1) != s.charAt(s.length() - idx--)) return false;
        }
 
        return true;
    }   
}
