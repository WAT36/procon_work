package Atcoder.abc_ontime;

import java.util.Scanner;

public class D_126_EvenRelation {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[][] t = new int[N+1][N+1];
		for(int i=1;i<N+1;i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();

			t[u][v] = w;
		}

		String[] c = new String[N+1];
		c[1] = "0";
		for(int i=1;i<N;i++) {
			for(int j=i+1;j<N;j++) {

				if(t[i][j] != 0) {
					if(t[i][j] % 2 == 0) {

					}else {

					}
				}
			}
		}
	}
}
