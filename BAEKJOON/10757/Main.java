// https://www.acmicpc.net/problem/10757

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        String[] input = new Scanner(System.in).nextLine().split(" ");
        
        BigInteger a = new BigInteger(input[0]);
        BigInteger b = new BigInteger(input[1]);

        return a.add(b).toString();
    }
}
