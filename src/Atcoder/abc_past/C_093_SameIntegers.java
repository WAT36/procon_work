package Atcoder.abc_past;

import java.util.Scanner;

public class C_093_SameIntegers {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();

		int max = Math.max(A, Math.max(B, C));
		int min = Math.min(A, Math.min(B, C));
		int med = (A + B + C) - max - min;

		int max_min_2 = max - min;
		int max_med_2 = max - med;

		int ans = 0;

		int temp = max_min_2 / 2;
		ans += temp;
		temp = max_med_2 / 2;
		ans += temp;

		if ((max_min_2 % 2) == (max_med_2 % 2)) {
			ans += max_min_2 % 2;
		} else {
			ans += 2;
		}
		System.out.println(ans);
	}
}
