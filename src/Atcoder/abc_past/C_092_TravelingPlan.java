package Atcoder.abc_past;

import java.util.Scanner;

public class C_092_TravelingPlan {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] A = new int[N+2];
		int sum=0;
		A[0] = 0;
		for(int i=1;i<N+1;i++) {
			A[i] = sc.nextInt();
			sum += Math.abs(A[i] - A[i-1]);
		}
		A[N+1] = 0;
		sum += Math.abs(A[N+1] - A[N]);

		for(int i=1;i<N+1;i++) {
			int ans = sum - Math.abs(A[i] - A[i-1]) - Math.abs(A[i+1] - A[i]) + Math.abs(A[i+1] - A[i-1]);
			System.out.println(ans);
		}
	}
}
