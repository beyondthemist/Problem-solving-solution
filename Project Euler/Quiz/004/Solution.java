// https://euler.synap.co.kr/quiz=4

public class Solution {
    public static void main(String args[]) {
        System.out.println(run());
    }
    
    public static String run() {
        int n = 100000000;
        StringBuilder sb = new StringBuilder();
 
        sb.append((char)('A' + (((26 + ((n%26) - 1)))%26)));
        while((n /= 26)) > 26) { sb.append((char)('A' + (((26 + ((n%26) - 1)))%26)));}
        sb.append((char)('A' + (((26 + ((n%26) - 1)))%26)));
 
        return sb.reverse().toString();
    }
}
