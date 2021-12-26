// https://euler.synap.co.kr/problem=14
// https://projecteuler.net/problem=14

public class Solution {
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        long temp;
        long result = 0;
        int max = 0;
        int count;
        
        for(int i = 2; i <= 1000000; ++i) {
            temp = i;
            count = 1;
            
            while (temp != 1) {
            	temp = ((temp%2 == 0) ? (temp / 2) : ((3*temp) + 1));
                ++count;
            }
            
            if(count > max) {
                max = count;
                result = i;
            }
            
        }
        
        return Long.toString(result);
    }
}
