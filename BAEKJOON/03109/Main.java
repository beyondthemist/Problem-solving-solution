import java.io.*;
import java.util.*;

public class Main  {
	static int count = 0;
	
	public static void main(String[] args)
	throws Exception {
		BufferedReader br = new BufferedReader(
			new InputStreamReader(System.in)
		);
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		char[][] grid = new char[r][c];

		for(int i = 0; i < r; ++i) {
			String row = br.readLine();
			for(int j = 0; j < c; ++j) {
				grid[i][j] = row.charAt(j);
			}
		}

		for(int i = 0; i < r; dfs(grid, i++, 0, r, c));

		System.out.println(count);
		
		br.close();
	}


	static boolean dfs(
		char[][] grid,
		int i,
		int j,
		int r,
		int c
	) {
		if(j == c - 1) {
			if(grid[i][j] != 'x') ++count;
			return true;
		}

		grid[i][j] = 'v';

		for(int offset = -1; offset <= 1; ++offset) {
			int nextI = i + offset, nextJ = j + 1;
			if(checkIndex(0, r, 0, c, nextI, nextJ) && grid[nextI][nextJ] == '.') {
				boolean res = dfs(grid, nextI, nextJ, r, c);
				if(res) return true;
			}
		}

		return false;
	}

	
	static boolean checkIndex(
		int rFrom,
		int rTo,
		int cFrom,
		int cTo,
		int i,
		int j
	) {
		return (rFrom <= i && i < rTo) && (cFrom <= j && j < cTo);
	}

}
