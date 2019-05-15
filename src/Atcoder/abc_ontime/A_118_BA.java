package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_118_BA {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String[] s = sc.nextLine().split(" ");

		int a = Integer.parseInt(s[0]);
		int b = Integer.parseInt(s[1]);

		if(b % a == 0) {
			System.out.println((a+b));
		}else {
			System.out.println((b-a));
		}
	}

}
