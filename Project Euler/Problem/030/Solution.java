// https://euler.synap.co.kr/problem=30
// https://projecteuler.net/problem=30

public class Solution {

	public static void main(String[] args) {
		System.out.println(run());
	}
	
	public static String run() {
		long sum = 0;
		
		for(int i = 2; i <= Integer.MAX_VALUE; ++i) {
			if(i == res(i)) { 
				sum += i; 
				System.out.println(i);
			}
		}
		
		return Long.toString(sum);
	}
	
	public static int res(int n) {
		int sum = 0;
		
		while(n != 0) {
			sum += exp5(n % 10);
			n /= 10;
		}
		
		return sum;
	}
	
	public static int exp5(int n) {
		return (n*n*n*n*n);
	}
}
