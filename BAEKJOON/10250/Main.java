//https://www.acmicpc.net/problem/10250
//20180224

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		run();
	}
	
	public static void run() {
		Scanner scanner = new Scanner(System.in);
		int t = scanner.nextInt();
		int[] h = new int[t];
		int[] w = new int[t];
		int[] n = new int[t];
		int count = 0;
		
		String[] result = new String[t];
		
		for(int i = 0; i < t; i++) {
			h[i] = scanner.nextInt();
			w[i] = scanner.nextInt();
			n[i] = scanner.nextInt();
		}
	
		for(int i = 0; i < t; i++) {
			count = 0;
			
			for(int j = 1; (j <= w[i]) && (count < n[i]); j++) {
				for(int k = 1; k <= h[i]; k++) {
					count++;
					
					if(count == n[i]) {
						if((1 <= j) && (j <= 9)) {
							result[i] = Integer.toString(k) + "0" +Integer.toString(j);
						} else {
							result[i] = Integer.toString(k) + Integer.toString(j);
						}
						
						break;
					}
				}
			}
			
		}
		
		for(int i = 0; i < t; i++) {
			System.out.println(result[i]);
		}
		
		scanner.close();
	}

}
