// https://euler.synap.co.kr/problem=22
// https://projecteuler.net/problem=22

import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
 
public class Solution {
    public static void main(String[] args) {
        System.out.print(run());
    }
    
    public static String run() {
        File file = new File("names.txt");
        int seq = 0, result = 0;
        List<String> list = new ArrayList<String>(0);

        try {
            FileReader fr = new FileReader(file);
            
            int b = -1;
            StringBuilder sb = new StringBuilder();
            while((b = fr.read()) != -1) {
                if(('A' <= b) && (b <= 'Z')) {
                    sb.append((char) b);
                } else if(b == ((int)',')) {
                    list.add(sb.toString());
                    sb = new StringBuilder();
                }
            } fr.close(); list.add(sb.toString()); //The last string doesn't contain a comma
            
            String[] arr = new String[list.size()];
            for(int i = 0; i < list.size(); arr[i] = list.get(i++));
            Arrays.sort(arr);
 
            for(int i = 0; i < arr.length; i++) {
                int sum = 0;
                for(int j = 0; j < arr[i].length(); j++) {
                    sum += (arr[i].charAt(j) - 'A' + 1);
                }
                
                result += (++seq*sum);
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        return Integer.toString(result);
    }
}
