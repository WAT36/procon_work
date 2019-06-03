package ARC20190330_EXAWizard;

import java.util.Scanner;

public class A_triangle {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();

		if(A == B && B == C) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}

}
