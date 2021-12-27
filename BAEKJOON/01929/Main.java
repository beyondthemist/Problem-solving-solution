// https://www.acmicpc.net/problem/1929

import java.util.Scanner;
 
public class Main {
    private final static int SIZE = 1000000;
    
    public static void main(String[] args) {
        run();
    }
    
    public static void run() {
        boolean[] isComp = new boolean[SIZE];
        int i, j;
        Scanner sc = new Scanner(System.in);
 
        isComp[0] = isComp[1] = true;
        for (i = 2; i < SIZE; ++i)
        {
            if (!isComp[i])
            {
                for (j = i << 1; j < SIZE; j += i)
                {
                    isComp[j] = true;
                }
            }
        }
 
        i = sc.nextInt();
        j = sc.nextInt();
 
        for (; i <= j; ++i)
        {
            if (!isComp[i])
            {
                System.out.println(i);
            }
        }    
        
        sc.close();
    }
 
}
