import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)
	throws Exception {
		BufferedReader br = new BufferedReader(
			new InputStreamReader(System.in, "UTF-8")
		);

		int t = Integer.parseInt(br.readLine());
		boolean[][] grid = new boolean[100 + 1][100 + 1];
		for(int tc = 0; tc < t; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());

			int[][] di = {
				{1, 0},
				{0, -1},
				{-1, 0},
				{0, 1}
			};
			grid[x][y] = true;

			x += di[d][0];
			y += di[d][1];
			grid[x][y] = true;

			List<Integer> moved = new ArrayList<>();
			moved.add(d);

			for(int gen = 1; gen <= g; ++gen) {
				List<Integer> toMove = new ArrayList<>();
				for(int i = moved.size() - 1; i >= 0; --i) {
					toMove.add((moved.get(i) + 1)%4);
				}

				for(int i = 0; i < toMove.size(); i++) {
					x += di[toMove.get(i)][0];
					y += di[toMove.get(i)][1];
				    grid[x][y] = true;
					moved.add(toMove.get(i));
				}
			}
		}

		int ans = 0;
		for(int i = 0; i < 100; i++) {
			for(int j = 0; j < 100; j++) {
				if(grid[i][j] & grid[i + 1][j] & grid[i][j + 1] & grid[i + 1][j + 1]) {
					++ans;
				}
			}
		}

		System.out.println(ans);
		br.close();
	}
}
