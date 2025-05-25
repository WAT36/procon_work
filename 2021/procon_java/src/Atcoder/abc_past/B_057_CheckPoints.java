package Atcoder.abc_past;

import java.util.Scanner;

public class B_057_CheckPoints {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[][] ab = new int[N][2];
		for(int i=0;i<N;i++) {
			ab[i][0] = sc.nextInt();
			ab[i][1] = sc.nextInt();
		}

		int[][] cd = new int[M][2];
		for(int i=0;i<M;i++) {
			cd[i][0] = sc.nextInt();
			cd[i][1] = sc.nextInt();
		}

		for(int i=0;i<N;i++) {
			int min = Integer.MAX_VALUE;
			int ans = 0;
			for(int j=0;j<M;j++) {
				int dist = Math.abs(ab[i][0] - cd[j][0]) + Math.abs(ab[i][1] - cd[j][1]);
				if(min > dist) {
					min = dist;
					ans = j+1;
				}
			}
			System.out.println(ans);
		}
	}
}
