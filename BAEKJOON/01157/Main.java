//https://www.acmicpc.net/problem/1157
//20180212

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {	
		System.out.println(new Main().run());
	}
	
	public String run() {
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		char temp;
		int[] alphabets = new int[26];
		int max = 0;
		String result = null;
		int idx = 0;
		
		for(int i = 0; i < input.length(); i++) {
			temp = input.charAt(i);
			
			//Upper case
			if((65 <= temp) && (temp <= 90)) {
				alphabets[temp - 65] += 1;
			//Lower case
			} else if((97 <= temp) && (temp <= 122)) {
				alphabets[temp - 97] += 1;
			}
		}
		
		for(int i = 0; i < alphabets.length; i++) {
			if(max < alphabets[i]) {
				max = alphabets[i];
				idx = i;
				result = Character.toString((char)(i + 65));
			}
		}
		
		for(int i = 0; i < alphabets.length; i++) {
			if(i != idx) {
				if(alphabets[i] == max) {
					result = "?";
					break;
				}
			}
		}
	
		scanner.close();
		
		return result;
	}
}
