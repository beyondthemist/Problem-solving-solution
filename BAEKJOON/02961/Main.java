import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)
	throws Exception {		
		BufferedReader br = new BufferedReader(
			new InputStreamReader(System.in)
		);
		int n = Integer.parseInt(br.readLine());
		int[] ss = new int[n];
		int[] bb = new int[n];
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			ss[i] = Integer.parseInt(st.nextToken()); 
			bb[i] = Integer.parseInt(st.nextToken());
		}

		int answer = solve(ss, bb, n, new boolean[n], 0);
		System.out.println(answer);

		br.close();
	}
	
	public static int solve(int[] ss, int[] bb, int n, boolean[] selected, int count) {
		if(count == n) {
			 int diff = Integer.MAX_VALUE;
			 int s = 1, b = 0;
			 for(int i = 0; i < n; i++) {
				 if(selected[i]) {
					 s *= ss[i];
					 b += bb[i];
				 }
			 }
			 if(s != 1 && b != 0) { 
				 diff = Math.abs(s - b);				 
			 }

			 return diff;
		}
		
		selected[count] = true;
		int a = solve(ss, bb, n, selected, count + 1);
		selected[count] = false;
		int b = solve(ss, bb, n, selected, count + 1);
		
		return Math.min(a, b);
	}
}
