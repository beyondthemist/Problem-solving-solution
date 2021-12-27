// https://euler.synap.co.kr/problem=23
// https://projecteuler.net/problem=23

public class Temp {
	private final static int MAXIMUM = 28123;
	
	public static void main(String[] args) {
		System.out.println(run());
	}
	
	public static String run() {
		int sum = 23*24/2;
		boolean legal = true;
		
		for(int i = 24; i < MAXIMUM; ++i) {
			for(int j = 12; j <= (i / 2); ++j) {
				if(isAbundant(j) && isAbundant(i - j)) {
					legal = false;
					break;
				}
			}
			
			if(legal) {
				sum += i;
			}
			
			legal = true;
		}
	
		return Integer.toString(sum);
	}

	public static boolean isAbundant(int num) {
		return isPrime(num) ? false : (d(num) > num);
	}
	
	//Sum of proper divisor
	public static int d(int num) {
		if(num == 1) { return 1; }
		
		int sum = 1;
		int lim = (int)(Math.sqrt(num));
		
		//if num is square number
		if(sqre(lim) == num) {
			sum += lim;
			lim--;
			
		}		
		
		//if num is square number i = 2, 3, ..., lim - 1
		//else i = 2, 3, ..., lim
		for(int i = 2; i <= lim && sum <= num; ++i) {
			if(num%i == 0) {
				sum += (i + num/i);
			}
		}
		
		return sum;
	}
	
	public static boolean isPrime(int num) {
		if(num < 0) {
			throw new IllegalArgumentException("Negative number");
		} else if(num == 0) {
			throw new IllegalArgumentException("Not a natural number");
		} else if(num == 1) {
			return false;
		} else if(num == 2) {
			return true;
		} else {
			if(num%2 == 0) {
				return false;
			} else {
				//Eratosthenes's sieve
				for(int i = 3; sqre(i) <= num; i += 2) {
					if(num%i == 0) {
						return false;
					}
				}
				
				return true;
			}
		}
		
	}
	
	//Square of number
	public static int sqre(int num) {
		return num*num;
	}
}
