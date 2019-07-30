package Atcoder.abc_past;

import java.util.Scanner;

public class A_AGC031_ColorfulSubsequence {

	public static final long MOD = 1000000007L;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.nextLine();
		String S = sc.nextLine();

		int[] alphabet = new int[26];
		for(int i=0;i<N;i++) {
			alphabet[(int)(S.charAt(i) - 97)]++;
		}

		long ans = 1;
		for(int i=0;i<26;i++) {
			ans = (ans % MOD) * ((alphabet[i] + 1) % MOD);
		}
		ans--;
		System.out.println(ans % MOD);
	}

}
