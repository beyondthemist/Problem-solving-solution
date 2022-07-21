//https://www.acmicpc.net/problem/10809
//20180212

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		new Main().run();
	}

	public void run() {
		int[] ab = new int[26];
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		
		for(int i = 0; i < ab.length; i++) {
			ab[i] = -1;
		}
		
		for(int i = 0; i < input.length(); i++) {
			if(ab[input.charAt(i) - 97] == -1) {
				ab[input.charAt(i) - 97] = i;
			}
		}
		
		
		for(int i = 0; i < ab.length; i++) {
			System.out.print(ab[i] + " ");
		}
	}
}
