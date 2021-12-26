// https://euler.synap.co.kr/problem=16
// https://projecteuler.net/problem=16

// Without library
public class Solution {
    private final static int A = 2; 
    private final static int N = 1000; 
    
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        int[] arr = new int[350];
        int sum = 0;
        
        /*Initialize array by -1*/
        for(int i = 0; i < (arr.length - 1); ++i) {
            arr[i] = -1;
        }
        
        arr[arr.length - 1] = 1;
        
        /*Repeat N times*/
        for(int i = 1; i <= N; ++i) {
            
            /*Multiple A*/
            for(int j = (arr.length -1); arr[j] >= 0; --j) {    
                arr[j] *= A;
            }
            
            for(int j = (arr.length -1); (arr[j] >= 0) && (j > 0); --j) {
                if(arr[j] >= 10) {
                    if(arr[j - 1] < 0) {
                        arr[j - 1] = (arr[j] / 10);
                    } else {
                        arr[j - 1] += (arr[j] / 10);
                    }
                    
                    arr[j] %= 10;
                }
            }
        }
        
        for(int i = 0; i < arr.length; ++i) {
            if(arr[i] != -1) { 
                sum += arr[i];
            }
        }
        
        return Integer.toString(sum);
    }
 
}
