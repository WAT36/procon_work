package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_120_Sound {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();

		if((B/A) > C) {
			System.out.println(C);
		}else {
			System.out.println(B/A);
		}

	}

}
