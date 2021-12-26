// https://euler.synap.co.kr/problem=19
// https://projecteuler.net/problem=19

public class Solution {
    
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        int sunday;
        int count = 0;
        int today = 1;
        
        for(int month = 1; month <= 12; month++) {
            switch(month) {
                case 1: case 3:  case 5: case 7: case 8: case 10: case 12:
                    today += 31;
                    break;
                case 2:
                    today += 28;
                    break;    
                case 4: case 6: case 9: case 11:
                    today += 30;
                    break;
                    
            }
        }
        
        sunday = 1 + (7 - (today % 7));
        
        for(int year = 1901; year <= 2000; year++) {
            for(int month = 1; month <= 12; month++) {                
                if(sunday == 1) { count++; }
                
                switch(month) {
                    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                        while(sunday <= 31) { 
                            sunday += 7;
                        }
                        
                        sunday -= 31;
                        break;
                    case 2:
                        if(((year%4 == 0) && (year%100 != 0)) || (year%400 == 0)) {
                            while(sunday < 29) {
                                sunday += 7;
                            }
                            
                            sunday -= 29;
                        } else {
                            while(sunday < 28) {
                                sunday += 7;
                            }
                            
                            sunday -= 28;
                        }
                        break;
                    case 4: case 6: case 9: case 11:                    
                        while(sunday <= 30) {
                            sunday += 7;
                        }
                        
                        sunday -= 30;
                        break;
                }
            }
        }
        
        return Integer.toString(count);
    }
}
