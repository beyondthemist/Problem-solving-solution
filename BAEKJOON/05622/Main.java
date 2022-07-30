//https://www.acmicpc.net/problem/5622
//20180212

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		System.out.println(new Main().run());
	}
	
	public String run() {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		int sum = 0;
		int c;
		
		for(int i = 0; i < input.length(); i++) {
			c = input.charAt(i);
			
			if((65 <= c) && (c <= 67)) { //ABC
				sum += 3;
			} else if((68 <= c) && (c <= 70)) { //DEF
				sum += 4;
			} else if((71 <= c) && (c <= 73)) { //GHI
				sum += 5;
			} else if((74 <= c) && (c <= 76)) { //JKL
				sum += 6;
			} else if((77 <= c) && (c <= 79)) { //MNO
				sum += 7;
			} else if((80 <= c) && (c <= 83)) { //PQRS
				sum += 8;
			} else if((84 <= c) && (c <= 86)) { //TUV
				sum += 9;
			} else if((87 <= c) && (c <= 90)) {//WXYZ
				sum += 10;
			}
		}
		
		sc.close();
		
		return Integer.toString(sum);
	}
	
}
