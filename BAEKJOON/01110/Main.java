import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int input = scanner.nextInt();
		int n1 = input / 10;
		int n2 = input % 10;
		int n3 = (n1 + n2) % 10;
		int temp = (10 * n2) + n3;
		int count = 1;
		
		while(input != temp) {
			count += 1;
			
			n1 = temp / 10;
			n2 = temp % 10;
			n3 = (n1 + n2) % 10;
			temp = (10 * n2) + n3;
		}
		
		System.out.print(count);
		
		scanner.close();
	}

}
