// https://euler.synap.co.kr/problem=35
// https://projecteuler.net/problem=35

public class Solution {
    public static void main(String args[]) {
        System.out.println(run());
    }
    
    public static String run() {
        int count = 0;
        int n = 1000000;
        boolean[] isComposite = new boolean[n + 1];
        
        for(int i = 2; i*i <= n; i++) {
            if(!isComposite[i]) {
                for(int j = i << 1; j < isComposite.length; j += i) {
                    isComposite[j] = true;
                }
            }
        }
        
        do {
            char[] num = Integer.toString(n).toCharArray();
            boolean result = true;
            
            for(int i = 0; i < num.length; i++) {
                char temp = num[num.length - 1];
                for(int j = num.length - 1; j >= 1; num[j] = num[j-- -1]);
                num[0] = temp;
                
                if(isComposite[Integer.parseInt(new String(num))]) {
                    result = false;
                    break;
                }
            }
             
            if(result) ++count;
        } while(--n > 1);
        
        return Integer.toString(count);
    }
}
