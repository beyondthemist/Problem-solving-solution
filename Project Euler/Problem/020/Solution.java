// https://euler.synap.co.kr/problem=20
// https://projecteuler.net/problem=20

public class Problem020 {    
    public static void main(String[] args) {
        System.out.println(run());
    }
    
    public static String run() {
        int[] arr = new int[158];
        int sum = 0;
 
        for(int i = 0; i < arr.length; ++i) {
            arr[i] = -1;
        }
        
        arr[arr.length - 1] = 1;
        
        for(int i = 1; i <= 100; ++i) {
            
            for(int j = (arr.length - 1); arr[j] >= 0; --j) {
                arr[j] *= i;
            }
            
            for(int j = (arr.length -1); (arr[j] >= 0) && (j >= 1); --j) {
 
                if((10 <= arr[j]) && (arr[j] <= 99)) {
                    if(arr[j - 1] < 0) {
                        arr[j - 1] = (arr[j] / 10);
                    } else {
                        arr[j - 1] += (arr[j] / 10);
                    }
                    
                    arr[j] %= 10;
                } else if((100 <= arr[j]) && (arr[j] <= 999)) { 
                    if((arr[j - 2] < 0) && (arr[j - 1] < 0)) {
                        arr[j - 2] = (arr[j] / 100);
                        arr[j - 1] = ((arr[j] % 100) / 10);
                        arr[j] %= 10;
                    } else if((arr[j - 2] < 0) && (arr[j - 1] >= 0)) {
                        arr[j - 2] = (arr[j] / 100);
                        arr[j - 1] += ((arr[j] % 100) / 10);
                        arr[j] %= 10;
                    } else if((arr[j - 2] >= 0) && (arr[j - 1] < 0)) {
                        arr[j - 2] += (arr[j] / 100);
                        arr[j - 1] = ((arr[j] % 100) / 10);
                        arr[j] %= 10;
                    } else if((arr[j - 2] >= 0) && (arr[j - 1] >= 0)) {
                        arr[j - 2] += (arr[j] / 100);
                        arr[j - 1] += ((arr[j] % 100) / 10);
                        arr[j] %= 10;
                    }
                }
            }
        }
        
        for(int i = 0; i < arr.length; ++i) {
            if(arr[i] >= 0) {
                sum += arr[i];
            }
        }
        
        return Integer.toString(sum);
    }
}
