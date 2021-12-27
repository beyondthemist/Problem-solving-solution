// https://euler.synap.co.kr/problem=24
// https://projecteuler.net/problem=24

import java.util.ArrayList;
import java.util.List;
 
public class Solution {
    public final static int LIMIT = 1000000;
    
    public static void main(String[] args) {
        run();
    }
    
    public static void run() {
        int count = 0;
        List<Integer> list = new ArrayList<Integer>(); 
        
        for(int i = 0; i <= 9; ++i) {
            for(int j = 0; j <= 9; ++j) {
                if(!list.contains(j)) {
                    count += factorial(9 - i);
                }
                
                if(count >= LIMIT) {
                    count -= fac(9 - i);
                    list.add(j);
                    break;
                }
            }
        }
        
        for(int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i));
        }
    }
    
    public static int factorial(int num) {
        int result = 1;
        
        for(int i = 2; i <= num; ++i) {
            result *= i;
        }
        
        return result;
    }
}
