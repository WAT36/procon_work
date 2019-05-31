package yuki;

import java.util.Scanner;

public class No0820_PowerOfTwo {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();

		int ans = (int)(Math.pow(2, N)/Math.pow(2, K));

		System.out.println(ans);
	}

}
