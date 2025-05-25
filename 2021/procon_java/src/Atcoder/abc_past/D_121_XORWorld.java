package Atcoder.abc_past;

import java.util.Scanner;

public class D_121_XORWorld {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long A = sc.nextLong();
		long B = sc.nextLong();

		System.out.println(f(A-1) ^ f(B));

	}

	public static long f(long A) {
		long n = A/4;
		switch((int)(A%4)) {
		case 0:
			return 4*n;
		case 1:
			return 1;
		case 2:
			return 4*n + 3;
		case 3:
			return 0;
		default:
			return 0;
		}
	}

}
