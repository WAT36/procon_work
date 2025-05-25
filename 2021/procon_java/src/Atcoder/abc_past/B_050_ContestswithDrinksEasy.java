package Atcoder.abc_past;

import java.util.Scanner;

public class B_050_ContestswithDrinksEasy {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] T = new int[N];
		int tsum = 0;
		for(int i=0;i<N;i++) {
			T[i] = sc.nextInt();
			tsum += T[i];
		}

		int M = sc.nextInt();
		int[] P = new int[M];
		int[] X = new int[M];
		for(int i=0;i<M;i++) {
			P[i] = sc.nextInt();
			X[i] = sc.nextInt();
		}

		for(int i=0;i<M;i++) {
			int ans = tsum;
			ans -= T[P[i]-1];
			ans += X[i];
			System.out.println(ans);
		}
	}
}
