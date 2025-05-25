package Atcoder.abc_past;

import java.util.Scanner;

public class A_111 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String n = sc.next();

		n = n.replace('9', '*');
		n = n.replace('1', '9');
		n = n.replace('*', '1');
		System.out.println(n);
	}
}
