// https://euler.synap.co.kr/problem=25
// https://projecteuler.net/problem=25

public class Solution {
	public static void main(String[] args) {
		System.out.println(new Problem025().run());
	}
	
	public String run() {
		int[] n1 = new int[1001];
		int[] n2 = new int[1001];
		int[] n3 = new int[1001];
		int lim = n3.length - 1;
		int count = 2;

		//Initialize all array by -1
		for(int i = 0; i < n1.length; i++) {
			n1[i] = -1; 
			n2[i] = -1;
			n3[i] = -1;
		}
		
		n1[lim] = 1;
		n2[lim] = 1;
		
		while(n3[1] < 0) {
			for(int i = lim; ((n1[i] >= 0) || (n2[i] >= 0)) && (i > 0); i--) {
				if(n1[i] < 0) {
					n1[i] = 0;
					n3[i] = n1[i] + n2[i];
				} else if(n2[i] < 0){
					n2[i] = 0;
					n3[i] = n1[i] + n2[i];
				}
				
				n3[i] = n1[i] + n2[i];
			}

			for(int i = lim; (n3[i] >= 0) && (i > 0); i--) {
				if(n3[i] >= 10) {
					if(n3[i - 1] < 0) {
						n3[i - 1] = (n3[i] / 10);
					} else {
						n3[i - 1] += (n3[i] / 10);
					}
					
					n3[i] %= 10;
				}
			}
			
			for(int i = lim; ((n1[i] >= 0) || (n2[i] >= 0) || (n3[i] >= 0)) && (i > 0); i--) {
				n1[i] = n2[i];
				n2[i] = n3[i];
			}
			
			count += 1;
		}
		
		return Integer.toString(count);
	}
}
