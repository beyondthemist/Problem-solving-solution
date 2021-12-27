// https://www.acmicpc.net/problem/2747

import java.util.Scanner;
 
public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        switch(n) {
        case 1: case 2:
            System.out.println(1);
            break;
        default:        
            int n1 = 1;
            int n2 = 1;
            int n3 = n1 + n2;
                
            for(int i = 3; i < n; ++i) {
                n1 = n2;
                n2 = n3;
                n3 = n1 + n2;
            }
            System.out.println(n3); 
        }
        
        sc.close();
    }
}

/*Another solution*/
/*
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(seq(sc.nextInt()));
        sc.close();
    }
    
    public static int seq(int n) {
        switch(n) {
        case 0: case 1:
            return n;
        default:
            return (seq(n - 1) + seq(n - 2));
        }
    }
} 
*/
