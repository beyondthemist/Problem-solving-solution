// https://euler.synap.co.kr/problem=92
// https://projecteuler.net/problem=92

public class Solution {
    public static void main(String args[]) {
        System.out.println(run());
    }
    
    public static String run() {
        int n = 9999999;
        int count = 0;
        
        while(n > 0) {
            int temp = n--;
            int sum;
 
            do {
                sum = 0;
                
                while(temp > 0) {
                    sum += ((temp%10)*(temp%10));
                    temp /= 10;
                }
 
                temp = sum;
            } while((sum != 1) && (sum != 89));
            
            if(sum == 89) { ++count; }
        }
        
        return Integer.toString(count);
    }
}
