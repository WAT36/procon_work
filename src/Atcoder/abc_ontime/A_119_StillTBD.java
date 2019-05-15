package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_119_StillTBD {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		int y = Integer.parseInt(s.substring(0, 4));
		int m = Integer.parseInt(s.substring(5, 7));
		int d = Integer.parseInt(s.substring(8, 10));

		if(y < 2019) {
			System.out.println("Heisei");
		}else if(y == 2019 && m < 4) {
			System.out.println("Heisei");
		}else if(y == 2019 && m == 4 && d <= 30) {
			System.out.println("Heisei");
		}else {
			System.out.println("TBD");
		}
	}
}
