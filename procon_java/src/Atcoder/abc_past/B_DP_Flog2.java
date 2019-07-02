package Atcoder.abc_past;

import java.util.Scanner;

public class B_DP_Flog2 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();

		int[] h = new int[N];
		long[] dp = new long[N];
		for(int i=0;i<N;i++) {
			h[i] = sc.nextInt();
			dp[i] = Long.MAX_VALUE;
		}
		dp[0] = 0;
		dp[1] = Math.abs(h[1] - h[0]);

		for(int i=2;i<N;i++) {
			for(int j = Math.max(0, i-K);j<i;j++) {
				dp[i] = Math.min(dp[i], dp[j] + Math.abs(h[j] - h[i]));
			}
		}
		System.out.println(dp[N-1]);
	}
}
