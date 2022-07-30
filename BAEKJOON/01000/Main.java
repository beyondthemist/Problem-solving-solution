//https://www.acmicpc.net/problem/1000

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[] arr = new int[2];
		int sum = 0;
		
		for(int i = 0; i < arr.length; i++) {
			sum += arr[i] = scanner.nextInt();
		}
		
		System.out.print(sum);
		
		scanner.close();
	}
}
