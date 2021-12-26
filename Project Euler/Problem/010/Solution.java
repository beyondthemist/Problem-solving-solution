// https://euler.synap.co.kr/problem=10
// https://projecteuler.net/problem=10

public class Problem010 {
    private static final int LIMIT = 2000000;
    
    public static void main(String[] args) {
        System.out.println(new Problem010().run());
    }
    
    public String run() {
        boolean[] isNotPrime = new boolean[LIMIT];
        int lim = (int) Math.sqrt((double) LIMIT);
        long sum = 0;
        
        for(int i = 2; i < lim; i++) {
            if(isNotPrime[i] == false) {
                for(int j = 2*i; j < LIMIT; j += i) {
                    isNotPrime[j] = true;
                }
            }
        }
        
        for(int i = 0; i < LIMIT; i++) {
            if(!isNotPrime[i]) {
                sum += i;
            }
        }
        
        return Long.toString(sum);
    }
 
}
