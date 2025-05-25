package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_190601_MSOL_Sumo {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();

		int k = S.length();
		int o = 0;
		int x = 0;
		for(int i=0;i<k;i++) {
			if(S.charAt(i) == 'o') {
				o++;
			}else {
				x++;
			}
		}

		if(k < 8) {
			System.out.println("YES");
		}else if(o >= k-7) {
			System.out.println("YES");
		}else {
			System.out.println("NO");
		}
	}
}
