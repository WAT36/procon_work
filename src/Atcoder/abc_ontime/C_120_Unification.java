package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_120_Unification {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		StringBuilder s = new StringBuilder().append(sc.nextLine());

		int ans = 0;
		int i = 0;
		while(i<s.length()-1) {
			if(s.substring(i, i+2).equals("01") ||
			   s.substring(i, i+2).equals("10")) {
				s = s.delete(i, i+2);
				ans += 2;
				if(i > 0) i--;
			}else {
				i++;
			}
		}
		System.out.println(ans);
	}
}
