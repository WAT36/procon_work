package Atcoder.abc_past;

import java.util.Scanner;

public class D_125_FlipingSigns {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		long[] A = new long[N];

		long sum_a = 0;
		int minus_count = 0;
		long min_abs = Long.MAX_VALUE;
		boolean zero = false;
		for(int i=0;i<N;i++) {
			A[i] = sc.nextLong();
			sum_a += Math.abs(A[i]);
			if(A[i] == 0) {
				zero = true;
			}else if(A[i] < 0) {
				minus_count++;
			}

			if(Math.abs(A[i]) < min_abs) {
				min_abs = Math.abs(A[i]);
			}
		}

		if(zero) {
			System.out.println(sum_a);
		}else if(minus_count % 2 == 0) {
			System.out.println(sum_a);
		}else {
			System.out.println(sum_a - 2*min_abs);
		}
	}
}
