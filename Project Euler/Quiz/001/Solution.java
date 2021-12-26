// https://euler.synap.co.kr/quiz=1

public class Main {
    public static void main(String args[]) {
      System.out.println(run());
    }
 
    public static String run() {
        long n = 9999 + 1;
        long count1 = 0;
        long count2 = 0;
 
        while(--n > 0) {
            String temp = Long.toString(n);
            long sum;
            do {
                sum = 0;
                for(int i = 0; i < temp.length(); i++) {
                    long a = (long)(temp.charAt(i) - '0');
                    sum += (a*a);
                }
 
                
                if(sum == 1) {
                    ++count1;
                    count2 += ((long)n);
                } else {
                    temp = Long.toString(sum);
                }
 
            } while((sum != 1) && (sum != 89));
        }
 
        return Long.toString(count1*count2);
    }
}
