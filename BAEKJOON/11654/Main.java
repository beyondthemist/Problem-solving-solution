// https://www.acmicpc.net/problem/11654
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        new Main().run();
    }
    
    public void run() {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        int c = input.charAt(0);
        
        System.out.println(c);
        
        scanner.close();
    }
}
/* Solution 2 */
/*
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
            System.out.println((int)(scanner.next().charAt(0)));
            scanner.close();
    }
}
*/

/* Solution 3 */
/*
public class Main {
    public static void main(String[] args) {
        System.out.println((int)(new java.util.Scanner(System.in).next().charAt(0)));
    }
}
*/
