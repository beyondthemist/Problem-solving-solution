//https://www.acmicpc.net/problem/2292

import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        System.out.print(new Main().run());
    }
    
    public String run() {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        int count = 1;
        
        if(n == 1L) {
            scanner.close();
            
            return "1";
        }
        
        for(long na = 0L, nb = 1L, a = 0L, b = 1L; ; na += a, nb += b) {
            count++;
            
            if((6*na + 2 <= n) && (n <= 6*nb + 1)) {
                break;
            }
            a++;
            b++;
            
        }
        
        scanner.close();
        
        return Integer.toString(count);
    }
 
}
