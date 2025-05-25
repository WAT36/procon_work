package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_190615_diverta2 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();

		if(K == 1) System.out.println(0);
		else System.out.println(N-K);
	}
}