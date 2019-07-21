package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_134_GoldenApple {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int D = sc.nextInt();

		int ans = (int) Math.ceil((double) N / (double) (2*D + 1));
		System.out.println(ans);
	}
}
