package Atcoder.abc_past;

import java.util.Scanner;

public class D_DP_Knapzack1 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int W = sc.nextInt();
		int[] w = new int[N];
		int[] v = new int[N];
		long[][] dp = new long[N+1][W+1];
		for(int i=0;i<N;i++) {
			w[i] = sc.nextInt();
			v[i] = sc.nextInt();
		}

		for(int i=0;i<N;i++) {
			for(int j=0;j<=W;j++) {
				if(j < w[i]) {
					dp[i+1][j] = dp[i][j];
				}else {
					dp[i+1][j] = Math.max(dp[i][j-w[i]] + v[i], dp[i][j]);
				}
			}
		}

		System.out.println(dp[N][W]);
	}
}
