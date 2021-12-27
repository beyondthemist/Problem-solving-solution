// https://euler.synap.co.kr/problem=37
// https://projecteuler.net/problem=37

public class Solution { 
    public static void main(String[] args) {
        System.out.println(run());
    }
 
    public static String run() {
        int n = 11;
        String temp;
        boolean prime;
        int sum = 0;
        int len;
        
        for(int count = 1; count <= 11; n++) {
            if(isPrime(n)) {
                temp = Integer.toString(n);
                len = temp.length();
                prime = true;
                
                //from left
                for(int j = 1; j <= (len - 1); j++) {
                    if(!isPrime(Integer.parseInt(temp.substring(0, j)))) {
                        prime = false;
                        break;
                    }
                }
                
                if(prime) {
                    //from right
                    for(int j = 1; j < len; j++) {
                        if(!isPrime(Integer.parseInt(temp.substring(len - j, len)))) {
                            prime = false;
                            break;
                        }
                    }
                }
                
                if(prime) {
                    sum += n;
                    ++count;
                }
            }
 
        }
 
        return Integer.toString(sum);
    }
 
    public static boolean isPrime(int n) {
        switch(n) {
        case 0: case 1:
            return false;
            
        case 2: 
            return true;
 
        default:
          if(n%2 == 0) { return false; }
            else {
                for(int i = 3; i*i <= n; i += 2) {
                    if(n%i == 0) { return false; }
                }
            }
 
            return true;
        }
    }
}
