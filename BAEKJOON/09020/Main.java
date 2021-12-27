//https://www.acmicpc.net/problem/9020

import java.util.Scanner;
 
public class Main {
    
    public static void main(String[] args) {
        run();
    }
    
    public static void run() {
        int t;
        boolean[] isComp = new boolean[10001];
        Scanner scanner = new Scanner(System.in);
        int a = -1, b = -1;
        int[] n;
        
        t = scanner.nextInt();
        n = new int[t];
        
        for(int i = 2; i < isComp.length; ++i) {
            if(!isComp[i]) {
                for(int j = i << 1; j < isComp.length; j += i) {
                    isComp[j] = true;
                }
            }
        }
        
        for(int i = 0; i < t; ++i) {
            n[i] = scanner.nextInt();
        }    
        
        for(int i = 0; i < t; ++i) {
            for(int j = 2; j <= n[i]/2; ++j) {
                if(!(isComp[j] || isComp[n[i] - j])) {
                    a = j; 
                    b = n[i] - j;
                }
            }
        
            System.out.printf("%d %d\n", a, b);
        }
        
        scanner.close();
    }
}
