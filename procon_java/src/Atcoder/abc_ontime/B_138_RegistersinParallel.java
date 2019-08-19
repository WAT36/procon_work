package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_138_RegistersinParallel {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] a = new long[N];

		double invsum = 0;
		for (int i = 0; i < N; i++) {
			a[i] = sc.nextLong();
			invsum += 1.0 / (double) a[i];
		}
		System.out.println(1.0 / invsum);

		// long malsum = 1;
		// for(int i=0;i<N;i++) {
		// a[i] = sc.nextLong();
		// malsum *= a[i];
		// }
		//
		// long sum = 0;
		// for(int i=0;i<N;i++) {
		// sum += malsum / a[i];
		// }
		//
		// System.out.println((double)malsum/(double)sum);
	}

}
