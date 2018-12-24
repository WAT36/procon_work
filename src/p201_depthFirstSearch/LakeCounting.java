package p201_depthFirstSearch;

import java.util.Random;

public class LakeCounting {

	public static final int M = 12; // たて
	public static final int N = 12; // 横
	public static final char lake = 'W';  // 池
	public static final char glass = '.'; // 草

	public char[][] map;

	public LakeCounting() {
		map = generate();
		print();
	}

	public void dfs(int i,int j) {

		if(i < 0 || i >= M || j < 0 || j >= N) {
			return ;
		}else if(map[i][j] == 'W') {
			map[i][j] = '.';
			dfs(i-1,j);
			dfs(i-1,j+1);
			dfs(i,j+1);
			dfs(i+1,j+1);
			dfs(i+1,j);
			dfs(i+1,j-1);
			dfs(i,j-1);
			dfs(i-1,j-1);
		}else {
			return ;
		}
	}

	public char[][] generate() {
		char[][] map = new char[M][N];

		Random r = new Random();
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (r.nextInt(2) == 0) {
					map[i][j] = 'W';
				} else {
					map[i][j] = '.';
				}
			}
		}

		return map;
	}

	public void print() {

		for(int i=0;i<map.length;i++) {
			for(int j=0;j<map[i].length;j++) {
				System.out.print(map[i][j]);
			}
			System.out.println();
		}
	}

	public static void main(String args[]) {

		LakeCounting l = new LakeCounting();
		int lakecount = 0;

		long start = System.currentTimeMillis();
		for(int i=0;i<M;i++) {
			for(int j=0;j<N;j++) {
				if(l.map[i][j] == 'W') {
					lakecount++;
				}
				l.dfs(i, j);
			}
		}
		long stop = System.currentTimeMillis();
		System.out.println("実行時間："+(stop - start)+"ms");
		System.out.println(lakecount);
	}

}
