package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_126_YYMM {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		String S = sc.nextLine();

		int a = Integer.parseInt(S.substring(0, 2));
		int b = Integer.parseInt(S.substring(2, 4));

		if(1 <= a && a <= 12) {
			if(1<= b && b <= 12) {
				System.out.println("AMBIGUOUS");
			}else {
				System.out.println("MMYY");
			}
		}else {
			if(1<= b && b <= 12) {
				System.out.println("YYMM");
			}else {
				System.out.println("NA");
			}
		}
	}
}
