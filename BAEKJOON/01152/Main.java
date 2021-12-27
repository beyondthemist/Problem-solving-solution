//https://www.acmicpc.net/problem/1152

import java.util.Scanner;
import java.util.StringTokenizer;
 
public class Main { 
    public static void main(String[] args) {
        System.out.print(run());
    }
 
    public static String run() {
        Scanner scanner = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(scanner.nextLine(), " ");
        scanner.close();
        
        return Integer.toString(st.countTokens());
    }
}
