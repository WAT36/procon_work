package Atcoder.abc_past;

import java.util.Scanner;

public class C_067_SplitingPie {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[] a = new int[N];
		long sum = 0;
		for(int i=0;i<N;i++) {
			a[i] = sc.nextInt();
			sum += a[i];
		}

		long min = Integer.MAX_VALUE;
		long sum_order = 0;
		for(int i=0;i<N-1;i++) {
			sum_order += a[i];
			sum -= a[i];
			long diff = Math.abs(sum_order - sum);

			if(min > diff) {
				min = diff;
			}
		}
		System.out.println(min);
	}

}
