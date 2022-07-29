//https://www.acmicpc.net/problem/11720
//20180206

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String input = sc.next();
		int sum = 0;

		if(input != null) {
			for(int i = 0; i < n; i++) {
				sum += input.charAt(i) - '0';
			}
		}
		
		System.out.println(sum);
		
		sc.close();
	}
}
