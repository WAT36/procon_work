package Atcoder.abc_past;

import java.util.Scanner;

public class C_102_LinearApproximation {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		sc.nextLine();
		String[] s = sc.nextLine().split(" ");

		long[] a = new long[N];
		long sum_a = 0;
		for(int i=0;i<N;i++) {
			a[i] = Long.parseLong(s[i]);
			sum_a += a[i];
		}

		long b = (-(N+1) / 2) + (sum_a / N);

		int ans = 0;
		for(int i=0;i<N;i++) {
			ans += Math.abs(a[i] - (b + (i+1)));
		}

		System.out.println(ans);
	}

}
