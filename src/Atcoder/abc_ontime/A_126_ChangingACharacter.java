package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_126_ChangingACharacter {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();

		sc.nextLine();
		String S = sc.nextLine();

		String ans = S.substring(0, K-1) + S.substring(K-1,K).toLowerCase() + S.substring(K, N);
		System.out.println(ans);
	}

}
