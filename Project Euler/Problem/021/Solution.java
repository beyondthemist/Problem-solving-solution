// https://euler.synap.co.kr/problem=21
// https://projecteuler.net/problem=21

public class Solution {
    public static void main(String[] args) {
        System.out.println(run());
    }

    public static String run() {
        int sum = 0;
        int b = 0;

        for(int a = 2; a <= 10000; ++a) {
            if(!isPrime(a)) {
                b = d(a);
                
                if((b != a) && (d(b) == a)) {
                    sum += a;
                }
            }
        }

        return Integer.toString(sum);
    }

    public static int d(int num) {
        int sum = 1;    
        int root = (int)(Math.sqrt(num));

        for(int i = 2; i <= root; ++i) { 
            if(num%i == 0) { 
                sum += (i + num/i);
            }
        }

        return sum;
    }

    public static boolean isPrime(int num) {
        if(num <= 1) {
            return false;
        } else if(num == 2) { 
            return true;
        } else {
            if(num % 2 == 0) {
                return false;
            } else {
                for (int i = 3; i*i <= num; i += 2) {
                    if (num % i == 0) {
                        return false;
                    }
                }

                return true;
            }
        }
    }

}
