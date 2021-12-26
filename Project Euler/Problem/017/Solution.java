// https://euler.synap.co.kr/problem=17
// https://projecteuler.net/problem=17

import java.util.HashMap;
import java.util.Map;
 
public class Solution {
 
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        Map<Integer, Integer> map = new HashMap<>();
        int result = "onethousand".length();
        int count = 1;
        
        String[] numbers1 = { 
                "one", "two", "three", "four", "five", 
                "six", "seven", "eight", "nine", "ten", 
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                "sixteen", "seventeen", "eighteen", "nineteen"
        };
        
        String[] numbers2 = {
                "twenty", "thirty", "forty", "fifty",
                "sixty", "seventy", "eighty", "ninety"
        };
        
        map.put(0,  "".length());
        for(int i = 0; i < numbers1.length; i++) { map.put(i + 1, numbers1[i].length()); }
        for(int i = 0; i < numbers2.length; i++) { map.put((i * 10) + 20, numbers2[i].length()); }
        map.put(100,  "hundredand".length());
        
        while(count < 20) {
            result += map.get(count);
            count++;
        }
        while(count < 100) {
            result += map.get((count/10)*10);
            result += map.get(count%10);
            count++;
        }
        while(count <= 999) {
            if(count%100 < 20) {
                result += map.get(count/100); 
                result += map.get(100); 
                result += map.get(count%100); 
            } else {
                result += map.get(count/100); 
                result += map.get(100); 
                result += map.get(((count%100)/10)*10); 
                result += map.get(count%10);
            }
            
            count++;
        }
        
        count = 100;
        while(count <= 900) {
            result -= "and".length();
            count += 100;
        }
        
        return Integer.toString(result);
    }
 
}
