package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_130_Rounding {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int X = sc.nextInt();
		int A = sc.nextInt();

		if(X < A) {
			System.out.println(0);
		}else {
			System.out.println(10);
		}
	}
}
