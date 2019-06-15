package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class C_113_ID {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[][] iyp = new int[M][3];
		String[] ans = new String[M];
		int[] count = new int[N+1];

		for(int i=0;i<M;i++) {
			int P = sc.nextInt();
			int Y = sc.nextInt();
			iyp[i] = new int[] {P,Y,i};
		}
		//配列の[1]の要素で比較・ソート
		Arrays.sort(iyp,(a,b)->Integer.compare(a[1],b[1]));
		for(int i=0;i<M;i++) {
			String temp = String.format("%06d%06d", iyp[i][0],++count[iyp[i][0]]);
			ans[iyp[i][2]] = temp;
		}

		for(int i=0;i<ans.length;i++) {
			System.out.println(ans[i]);
		}
	}
}
