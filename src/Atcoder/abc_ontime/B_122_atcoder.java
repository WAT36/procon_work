package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_122_atcoder {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		StringBuilder sb = new StringBuilder();
		StringBuilder temp = new StringBuilder();

		for (int i = 0; i < s.length(); i++) {

			String si = s.substring(i, i + 1);

			if (si.equals("A") || si.equals("T") || si.equals("G") || si.equals("C")) {
				temp.append(si);
			} else if (sb.length() < temp.length()) {
				sb.setLength(0);
				sb.append(temp.toString());
				temp.setLength(0);
			} else {
				temp.setLength(0);
			}
		}

		if (sb.length() < temp.length()) {
			sb.setLength(0);
			sb.append(temp.toString());
			temp.setLength(0);
		}

		System.out.println(sb.length());
	}

}
