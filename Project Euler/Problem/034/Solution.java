// https://euler.synap.co.kr/problem=34
// https://projecteuler.net/problem=34

public class Solution {
    public static void main(String args[]) {
        System.out.println(run());
    }
 
    public static String run() {
        int count = 0;
 
        for(int i = 10; i <= 1000000; i++) {
            int temp = i;
            int sum = 0;
 
            do {
                sum += factorial(temp%10);
                temp /= 10;
            } while(temp > 0);
 
            if(sum == i) {
                count += i;
            }
        }
 
        return Integer.toString(count);
    }
 
    public static int factorial(int n) {
        int res = 1;
        for(int i = 2; i <= n; res *= i++);
 
        return res;
    }
}
