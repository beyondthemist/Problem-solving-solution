// https://www.acmicpc.net/problem/10828

import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        run();
    }
 
    public static void run()  {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] stack = new int[t];
        int top = -1;
        String command;
        
        sc.nextLine(); //입력 버퍼에 남은 개행 처리
        for(int i = 0; i < t; ++i) {
            command = sc.nextLine();
            
            if(command.equals("size")) {
                System.out.println(top + 1);
            
            } else if(command.equals("empty")) {
                System.out.println((top == -1) ? 1 : 0);
            
            } else if(command.equals("top")) {
                System.out.println((top == -1) ? -1 : stack[top]);
            
            } else if(command.equals("pop")) {
                System.out.println((top == -1) ? -1 : stack[top--]);
            
            } else if(command.matches("push [0-9]*")) {
                stack[++top] = Integer.parseInt(command.substring(5));
            }
        }
    }
}
