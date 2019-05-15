package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_122_atgc {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		char c = sc.nextLine().trim().charAt(0);

		switch (c) {
		case 'A':
			System.out.println("T");
			break;
		case 'T':
			System.out.println("A");
			break;
		case 'C':
			System.out.println("G");
			break;
		case 'G':
			System.out.println("C");
			break;
		}
	}
}
