// https://euler.synap.co.kr/problem=33
// https://projecteuler.net/problem=33

public class Solution {
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        double val;
        int countNumer = 1, countDenom = 1;
        
        for(int i = 1; i <= 9; i++) {
            for(int k = 1; k <= 9; k++) {
                for(int j = i + k/9; j <= 9; j++) {
                    for(int l = ((j > i) ? 1 : (k + 1)); l <= 9; l++) {
                        val = (double)(10*i + k)/(double)(10*j + l);
                    
                        if(i == j) {
                            if(val == (double)k / (double)l) {
                                countNumer *= k;
                                countDenom *= l;
                            }
                        } else if(i == l) {
                            if(val == (double)k / (double)j) {
                                countNumer *= k;
                                countDenom *= j;
                            }
                        } else if(k == j) {
                            if(val == (double)i / (double)l) {
                                countNumer *= i;
                                countDenom *= l;
                            }
                        } else if(k == l) {
                            if(val == (double)i / (double)j) {
                                countNumer *= i;
                                countDenom *= j;
                            }
                        }
                    }   
                }   
            }   
        }
        
        return Integer.toString(countDenom / gcd(countNumer, countDenom));
    }
    
    public static int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a%b);
    }
    
}
