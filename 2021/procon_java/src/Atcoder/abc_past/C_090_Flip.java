package Atcoder.abc_past;

import java.util.Scanner;

public class C_090_Flip {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();
		long M = sc.nextLong();

		if (N == 1) {
			if (M == 1) {
				System.out.println(1);
			} else if (M == 2) {
				System.out.println(0);
			} else {
				System.out.println(M - 2);
			}
		} else if (N == 2) {
			System.out.println(0);
		} else {
			if (M == 1) {
				System.out.println(N - 2);
			} else if (M == 2) {
				System.out.println(0);
			} else {
				System.out.println((M - 2) * (N - 2));
			}
		}
	}
}
