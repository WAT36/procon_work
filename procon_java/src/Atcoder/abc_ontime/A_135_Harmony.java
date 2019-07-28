package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_135_Harmony {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();

		if((A+B)%2 == 0) {
			System.out.println((A+B)/2);
		}else {
			System.out.println("IMPOSSIBLE");
		}
	}

}
