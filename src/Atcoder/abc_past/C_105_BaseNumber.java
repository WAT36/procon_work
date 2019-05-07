package Atcoder.abc_past;

import java.util.Scanner;

public class C_105_BaseNumber {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long S = Long.parseLong(sc.nextLine());

		if(S == 0) {
			System.out.println("0");
			return;
		}

		StringBuilder t = new StringBuilder();
		while(S != 0) {
			if(S % 2 == 0) {
				t.append(0);
				S /= (-2);
			}else {
				t.append(1);
				S = (S-1)/(-2);
			}
		}

		t.reverse();

		System.out.println(t.toString());
	}
}
