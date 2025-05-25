package Atcoder.abc_ontime;

import java.util.Scanner;

public class measure {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		if (s.length() == 2) {
			System.out.println(s);
		} else {
			for (int i = s.length() - 1; i >= 0; i--) {
				System.out.print(s.charAt(i));
			}
		}
	}
}
