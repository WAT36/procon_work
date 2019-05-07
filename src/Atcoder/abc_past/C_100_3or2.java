package Atcoder.abc_past;

import java.util.Scanner;

public class C_100_3or2 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[] a = new int[N];
		int sum_log2 = 0;
		for(int i=0;i<N;i++) {
			a[i] =sc.nextInt();
			sum_log2 += log2(a[i]);
		}

		System.out.println(sum_log2);
	}

	public static int log2(int a) {

		if(a % 2 != 0) {
			return 0;
		}else {
			return 1 + log2(a/2);
		}
	}

}
