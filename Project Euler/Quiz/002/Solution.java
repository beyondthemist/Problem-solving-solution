// https://euler.synap.co.kr/quiz=2

import java.io.BufferedWriter;
import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;
 
public class Q002 {
    public static void main(String args[]) {
      System.out.println(run());
    }
    
    public static String run() {
        int sum = 0;
        int countSyllables, countWords;
        String[] subUnits = new String[]{"", "십", "백", "천"};
        String[] superUnits = new String[]{"", "만", "억", "조"};
        String[] values = new String[]{"", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"};
        
        try {
            BufferedReader br = new BufferedWriter(new FileWriter(/*Your file*/));
            
            String str = null;
            while((str = br.readLine()) != null) {
                str = str.replaceAll("[^\\d]+", "");
                int len = str.length();
                StringBuilder result = new StringBuilder();
                List<String> tokens = new ArrayList<String>(0);
                
                if(len%4 != 0) { tokens.add(str.substring(0, len%4)); }
                for(int i = 0;
                    i < len >> 2;
                    tokens.add(str.substring(len%4 + (i++ << 2), len%4 + (i << 2))));
                
                for(int i = 0; i < tokens.size(); i++) {
                    String token = tokens.get(i);
                    if(token.compareTo("0000") > 0) {
                        result.append(" ");
                        for(int k = 0; k < token.length() - 1; k++) {
                            char c = token.charAt(k);
                            if(c > '1') { result.append(values[c - '0']); }
                            if(c > '0') { result.append(subUnits[token.length() - 1 - k]); }
                        }
                        
                        result.append(values[token.charAt(token.length() - 1) - '0']);
                        result.append(superUnits[tokens.size() - 1 - i]);
                    }
                }
                
                String s = result.toString().replace(" 일만", " 만").trim() + "원";
                countSyllables = s.length() - ((countWords = s.split(" ").length) - 1);
                sum += (countSyllables*countWords);
            }
        } catch(Exception e) {
            return "-1";
        }
        
        return Integer.toString(sum);
    }
}
