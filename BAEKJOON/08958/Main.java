import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int t;
		String[] results = null;
		int[] scores = null;
		int score = 0;
		t = scanner.nextInt();
		
		results = new String[t];
		scores = new int[t];
		
		for(int i = 0; i < results.length; i++) {
			results[i] = scanner.next();
		}
		
		for(int i = 0; i < results.length; i++) {
			for(int j = 0; j < results[i].length(); j++) {
				if(results[i].charAt(j) == 'O') {
					score += 1;
					scores[i] += score;
				} else {
					score = 0;
				}
			}
			score = 0;
		}
		
		for(int i = 0; i < scores.length; i++) {
			System.out.println(scores[i]);
		}
		scanner.close();
	}

}
