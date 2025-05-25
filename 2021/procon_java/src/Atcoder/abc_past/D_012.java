package Atcoder.abc_past;

import java.util.Scanner;

public class D_012 {

	public static final int INF = 999999;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[][] d = new int[N][N];
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				if(i!=j) {
					d[i][j]=INF;
				}else {
					d[i][j]=0;
				}
			}
		}

		for(int i=0;i<M;i++) {
			int a=sc.nextInt();
			int b=sc.nextInt();
			int t=sc.nextInt();
			d[a-1][b-1]=t;
			d[b-1][a-1]=t;
		}

		for(int a=0;a<N;a++) {
			for(int b=0;b<N;b++) {
				for(int c=0;c<N;c++) {
					d[b][c]=Math.min(d[b][c], d[b][a]+d[a][c]);
				}
			}
		}

		int ans=INF;
		for(int i=0;i<N;i++) {
			int ans_i=0;
			for(int j=0;j<N;j++) {
				ans_i=Math.max(ans_i, d[i][j]);
			}
			ans=Math.min(ans, ans_i);
		}

		System.out.println(ans);
	}

}
