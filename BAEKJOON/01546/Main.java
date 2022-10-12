import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int[] arr = new int[n];
		double sum = 0;
		double m = 0;
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = scanner.nextInt();
		}
		
		m = (double) arr[0];
				 
		for(int i = 1; i < arr.length; i++) {
			if(m < (double) arr[i]) {
				m = (double) arr[i];
			}
		}
		
		for(int i = 0; i < arr.length; i++) {
			sum += ((arr[i] / m) * 100);
		}
		
		System.out.printf("%.2f", (sum / ((double)arr.length)));
		
		scanner.close();
	}

}
