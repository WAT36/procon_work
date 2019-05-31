package Atcoder.abc_past;

import java.util.Scanner;

public class B_104_AcCepted {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();

		boolean flag = true;

		int c=0;
		for(int i=0;i<S.length();i++) {

			if(i == 0) {
				if(S.charAt(0) != 'A') {
					flag = false;
					break;
				}
			}else if(i >= 2 && i < S.length() - 1) {
				if(S.charAt(i) == 'C') {
					c++;
				}else if(Character.isUpperCase(S.charAt(i))) {
					flag = false;
					break;
				}
			}else {
				if(Character.isUpperCase(S.charAt(i))) {
					flag = false;
					break;
				}
			}
		}

		if(c != 1) flag = false;

		if(flag) {
			System.out.println("AC");
		}else {
			System.out.println("WA");
		}
	}

}
