// https://euler.synap.co.kr/problem=28
// https://projecteuler.net/problem=28

public class Solution {
	private static final int LEN = 1001;
	private static final int LIM = (LEN / 2) + 1;
	
	public static void main(String[] args) {
		System.out.println(run());

	}
	
	public static String run() {
		int[] add = {8, 6, 4, 2};
		int[] mem = {1, 1, 1, 1};
		long count = -3;
		
		for(int i = 1; i <= LIM; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				count += mem[j];
				mem[j] += add[j];
				add[j] += 8;
			}

		}
		
		return Long.toString(count);
	}
}
