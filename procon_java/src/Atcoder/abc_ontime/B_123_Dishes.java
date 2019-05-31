package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_123_Dishes {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int[] time = new int[5];
		int sum = 0;
		int frac = 10;
		for (int i = 0; i < 5; i++) {
			time[i] = sc.nextInt();
			sum += ((time[i] - 1) / 10 + 1) * 10;

			if (time[i] % 10 != 0) {
				frac = Math.min(frac, (time[i] % 10));
			}
		}
		System.out.println(sum - (10 - frac));
	}
}
