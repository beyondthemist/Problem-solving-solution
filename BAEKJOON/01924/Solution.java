// https://www.acmicpc.net/problem/1924

import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int today = 0;
        int x = sc.nextInt();
        int y = sc.nextInt();
        int month = 1;
        
        
        for(month = 1; month < x; month++) {
            switch(month) {
                //31일까지 있는 달
                case 1: case 3:  case 5: case 7: 
                case 8: case 10: case 12:
                    today += 31;
                    break;
                //2월
                case 2:
                    today += 28;
                    break;    
                //30일까지 있는 달
                case 4: case 6: case 9: case 11:
                    today += 30;
                    break;
            }
        } 
        
        today += y;
    
        switch(today % 7) {
            case 1:
                System.out.println("MON");
                break;
                
            case 2:
                System.out.println("TUE");
                break;
                
            case 3:
                System.out.println("WED");
                break;
                
            case 4:
                System.out.println("THU");
                break;
                
            case 5:
                System.out.println("FRI");
                break;
                
            case 6:
                System.out.println("SAT");
                break;
                
            case 0:
                System.out.println("SUN");
                break;
        }
        
        sc.close();
    }
    
}
