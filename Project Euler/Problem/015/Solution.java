// https://euler.synap.co.kr/problem=15
// https://projecteuler.net/problem=15

public class Problem015 {
    private static final int ROWS = 20;
    private static final int COLS = 20;
    
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        long result = 1L;
        
        for(int i = 0; i < ROWS; ++i) { //(40!)/(20!20!)
            result *= (ROWS + COLS - i);
            result /= (i + 1); 
        }
        
        return Long.toString(result);
    }
    
}
