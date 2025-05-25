package Atcoder.abc_past;

import java.util.Scanner;

public class A_AGC024_Fairness {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long A = sc.nextLong();
		long B = sc.nextLong();
		long C = sc.nextLong();
		long K = sc.nextLong();

		long ans = (K%2 == 0) ? A-B : B-A;
		if(Math.abs(ans) > Math.pow(10, 18)) {
			System.out.println("Unfair");
		}else {
			System.out.println(ans);
		}
	}
}
