// https://euler.synap.co.kr/problem=2
// https://projecteuler.net/problem=2

public class Solution {
    public static void main(String[] args) {
        int n1 = 1, n2 = 2;
        int n3 = n1 + n2;
        int sum = 2;
        
        while(n3 <= 4000000) {
            n3 = n1 + n2;
            
            if(n3%2 == 0) {
                sum += n3;
            }
            
            n1 = n2;
            n2 = n3;
        }
        
        System.out.println("Sum:" + sum);
    }
 
}
