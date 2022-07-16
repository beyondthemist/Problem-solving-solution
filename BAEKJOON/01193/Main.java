// https://www.acmicpc.net/problem/1193

import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        System.out.print(run1());
        System.out.print(run2());
    }
 
    public String run1() {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int count = 0;
        int numer = 1, denom = 1;
        String result = null;
        
        for(int i = 1; count < input; i++) {
 
            if(i%2 == 0) {
                numer = 1;
                denom = i;
                        
                for(int j = 1; j <= i; j++, numer++, denom--) {
                    count++;
                        
                    if(count >= input) {
                        break;
                    }
                }
            } else {
                numer = i;
                denom = 1;
                        
                for(int j = 1; j <= i; j++, numer--, denom++) {
                    count++;
                        
                    if(count >= input) {
                        break;
                    }
                }
            }
                    
        }
        
        sc.close();
        
        result = Integer.toString(numer) + "/" + Integer.toString(denom);
        
        return result;
    }
 
 
  	public static String run2() {
       Scanner sc = new Scanner(System.in);
       int x = sc.nextInt();
       int n = 0;
        
       while(sum(++n) < x);
        
       int diff = x - sum(n - 1) - 1;
       return (n%2 == 0) ? ((1 + diff) + "/" + (n - diff))
                         : ((n - diff) + "/" + (1 + diff));
    }
	
    
    public static int sum(int n) {
        return (n*(n + 1))/2;
    }
}
