package Atcoder.abc_past;

import java.util.Scanner;

public class B_055_TrainingCamp {

	public static final long MOD = 1000000007L;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		long ans = 1;
		for(long i=1;i<=N;i++) {
			ans *= i;
			ans %= MOD;
		}
		System.out.println(ans);
	}
}
