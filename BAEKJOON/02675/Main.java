//https://www.acmicpc.net/problem/2675
//20180212

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		new Main().run();
	}
	
	public void run() {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt(); //Test case
		int[] r = new int[n]; //repeat
		String[] t = new String[n]; //
		
				
		for(int i = 0; i < n; i++) {
			r[i] = scanner.nextInt();
			t[i] = scanner.next();
		}
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < t[i].length(); j++) {
				for(int k = 0 ; k < r[i]; k++) {
					System.out.print(t[i].charAt(j));
				}
			}
			System.out.println();
		}
		
		scanner.close();
		
	}
}
