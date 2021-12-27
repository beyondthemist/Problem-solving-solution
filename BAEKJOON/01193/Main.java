// https://www.acmicpc.net/problem/1193

import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        System.out.print(new Main().run());
    }
 
    public String run() {
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
}
