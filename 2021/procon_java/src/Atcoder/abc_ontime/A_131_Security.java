package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_131_Security {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		for(int i=1;i<s.length();i++) {
			if(s.charAt(i-1) == s.charAt(i)) {
				System.out.println("Bad");
				return;
			}
		}
		System.out.println("Good");
	}
}
