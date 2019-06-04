package Atcoder.abc_past;

import java.util.Scanner;

public class B_100_Ringo {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int D = sc.nextInt();
		int N = sc.nextInt();

		if(N == 100) N = 101;
		System.out.println((long)(N * Math.pow(100, D)));
	}

}
