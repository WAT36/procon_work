package Atcoder.abc_past;

import java.util.Scanner;

public class C_058_DubiousDocument {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();

		int[] alpha = new int[26];
		for(int i=0;i<26;i++) {
			alpha[i] = Integer.MAX_VALUE;
		}

		for(int i=0;i<n;i++) {
			String S = sc.nextLine();

			int[] alpha_i = new int[26];
			for(int j = 0;j<S.length();j++) {
				alpha_i[S.charAt(j) - 97]++;
			}

			for(int j=0;j<26;j++) {
				if(alpha_i[j] < alpha[j]) {
					alpha[j] = alpha_i[j];
				}
			}
		}

		String ans ="";
		for(int i=0;i<26;i++) {
			String ansi = "";
			for(int j=0;j<alpha[i];j++) {
				char c = (char) (i + 97);
				ansi = ansi + String.valueOf(c);
			}
			ans = ans + ansi;
		}
		System.out.println(ans);
	}
}
