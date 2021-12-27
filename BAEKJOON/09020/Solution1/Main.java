import java.util.Arrays;
import java.util.Scanner;
 
public class Main {
    
    public static void main(String[] args) {
        run();
    }
    
    public static void run() {
        int t;
        int[] n;
        Scanner scanner = new Scanner(System.in);
        int a = -1, b = -1;
        
        t = scanner.nextInt();
        n = new int[t];
        
        for(int i = 0; i < t; ++i) {
            n[i] = scanner.nextInt();
        }
        
        for(int i = 0; i < t; ++i) {
            for(int j = 2; j <= n[i]/2; ++j) {
                if(isPrime(j) && isPrime(n[i] - j)) {
                    a = j; b = n[i] - j;
                }
            }
            
            System.out.printf("%d %d\n", a, b);
        }
        
        scanner.close();
    }
    
    public static boolean isPrime(int n) {
        if (n != 2) {
            if ((n % 2 == 1) && (n != 1)) {
                for (int i = 3; i*i <= n; i += 2) {
                    if (n%i == 0) { return false; }
                }
            } else { 
                return false; 
            }
        }
 
        return true;
    }
 
}
