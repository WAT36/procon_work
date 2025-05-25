package Atcoder.abc_past;

import java.util.Scanner;

public class C_ABC079_TrainChicket {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		int[] num = new int[4];

		num[0] = Integer.parseInt(s.substring(0, 1));
		num[1] = Integer.parseInt(s.substring(1, 2));
		num[2] = Integer.parseInt(s.substring(2, 3));
		num[3] = Integer.parseInt(s.substring(3, 4));

		String ans = calc(num, 0, "+", 0);
		if (ans.length() < 4) {
			System.out.println("");
		} else {
			String a = String.valueOf(num[0]);
			for (int i = 1; i <= 3; i++) {
				a = a + String.valueOf(ans.charAt(i));
				a = a + String.valueOf(num[i]);
			}
			a = a + "=7";
			System.out.println(a);
		}
	}

	public static String calc(int[] num, int numind, String op, int sum) {
		int n = num[numind];
		if (op.equals("-"))
			n *= -1;

		int newsum = sum + n;
		if (numind >= 3) {
			if (newsum == 7) {
				return op;
			} else {
				return "";
			}
		} else {
			String s = calc(num, numind + 1, "+", newsum);
			if (s.length() > 0) {
				return op + s;
			} else {
				s = calc(num, numind + 1, "-", newsum);
				if (s.length() > 0)
					return op + s;
				return s;
			}
		}
	}
}
