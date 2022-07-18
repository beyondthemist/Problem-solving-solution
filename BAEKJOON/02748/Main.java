//https://www.acmicpc.net/problem/2748
//20210227

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;

public class Main {
	public static void main(String[] args)
	throws Exception {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));	
		BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(input.readLine());
		BigInteger[] arr = new BigInteger[n + 1];
		
		arr[0] = BigInteger.ZERO; arr[1] = BigInteger.ONE;
		for(int i = 2; i <= n; arr[i] = arr[i - 1].add(arr[i++ - 2]));
		
		System.out.println(arr[n]);
		
		input.close();
		output.flush();
		output.close();
	}
}
