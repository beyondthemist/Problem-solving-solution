//https://www.acmicpc.net/submit/2775/7863976
//20190326

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		new Main().run();
	}

	public void run() {
		Scanner scanner = new Scanner(System.in);
		int t = scanner.nextInt();
		int[][] apt = new int[15][14];
		int[] result = new int[t];
		int sum = 0; 
		
		for(int j = 0; j < 14; j++) {
			apt[14][j] = j + 1;
		}
		
		for(int i = 13; i >= 0; i--) {
			for(int j = 0; j < 14; j++) {
				sum += apt[i + 1][j];
				apt[i][j] = sum;
			}
			
			sum = 0;
		}
		
		for(int i = 0; i < t; i++) {
			result[i] = apt[ 14 - scanner.nextInt() ][ scanner.nextInt() - 1 ];
		}
		
		for(int i = 0; i < t; i++) {
			System.out.println(result[i]);
		}
		
		
		scanner.close();
	}
}
