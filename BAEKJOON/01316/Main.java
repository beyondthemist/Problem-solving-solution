// https://www.acmicpc.net/problem/1316

import java.util.Scanner;

public class Main {
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in);
		
		int i = 0;
		int n = sc.nextInt();
		int answer = n;
		
		for(int test_case = 0; test_case < n; test_case++) {
			String word = sc.next();
			boolean[] checker = new boolean[26];
			
			for(i = 1; i < word.length(); i++) {
				if(word.charAt(i - 1) != word.charAt(i)) {
					if(checker[word.charAt(i) - 97] == true) {
						answer--;
						break;
					}
					
					checker[word.charAt(i - 1) - 97] = true;
				}
			}
		}
		
		System.out.println(answer);
		
	}
}
