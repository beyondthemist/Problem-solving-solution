# https://www.acmicpc.net/problem/2941

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args)
	throws Exception {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));	
		BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] arr = new String[] {
				"c=", "c-",
				"dz=", "d-",
				"lj", "nj",
				"s=", "z=",
		};
		
		String str = input.readLine();
		input.close();
		
		for(int i = 0; i < arr.length;str = str.replace(arr[i++], "A"));
		output.write(Integer.toString(str.length()));
		output.flush();
		output.close();
	}
}
