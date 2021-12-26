// https://euler.synap.co.kr/problem=12
// https://projecteuler.net/problem=12

public class Solution {
    public static void main(String[] args) {
        long beginTime = System.currentTimeMillis();
        System.out.println(run());
        long endTime = System.currentTimeMillis();
        
        System.out.println((endTime - beginTime) + "ms");
    }
    
    public static String run() {
        int n = 0;
        int triNum = 0;
        int max = 0;
        int divs = 0;
        int lim;
        
        while(divs < 500) {
            divs = 2;
            
            if(divs > max) {
                max = divs;
            }
            
            //삼각수 계산
            triNum += ++n;
            
            lim = (int)(Math.sqrt(triNum));
            
            //약수의 개수 계산
            if(triNum%2 != 0) { //삼각수가 홀수일 때
                for(int i = 3; i < lim; i += 2) {
                    if(triNum%i == 0) {
                        divs += 2;
                    }
                }
            } else { //삼각수가 짝수일 때
                for(int i = 2; i < lim; i += 1) {
                    if(triNum%i == 0) {
                        divs += 2;
                    }
                }
            }
        }
        
        return Integer.toString(triNum);
    }
}
