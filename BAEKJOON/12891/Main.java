import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)
	throws Exception {
		BufferedReader br = new BufferedReader(
			new InputStreamReader(System.in)
		);

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int p = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());

		char[] dnaStr = br.readLine().toCharArray();
		int[] targetCounts = new int[4];
		st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i < 4; i++) {
			targetCounts[i] = Integer.parseInt(st.nextToken());
		}

		int answer = 0;
		int[] counts = new int[4];
		int left = 0, right = left + (s - 1);
		for(int i = left; i <= right; i++) {
			switch(dnaStr[i]) {
			case 'A': ++counts[0]; break;
			case 'C': ++counts[1]; break;
			case 'G': ++counts[2]; break;
			case 'T': ++counts[3]; break;
			}
		}

		if(legal(counts, targetCounts)) {
			++answer;
		}
		
		while(right < p - 1) {
			switch(dnaStr[left++]) {
			case 'A': --counts[0]; break;
			case 'C': --counts[1]; break;
			case 'G': --counts[2]; break;
			case 'T': --counts[3]; break;
			}

			switch(dnaStr[++right]) {
			case 'A': ++counts[0]; break;
			case 'C': ++counts[1]; break;
			case 'G': ++counts[2]; break;
			case 'T': ++counts[3]; break;
			}

			if(legal(counts, targetCounts)) {
				++answer;
			}
		}

		System.out.println(answer);

		br.close();
	}

	public static boolean legal(int[] counts, int[] targetCounts) {
		for(int i = 0; i < 4; ++i) {
			if(counts[i] < targetCounts[i]) {
				return false;
			}
		}

		return true;
	}
}
