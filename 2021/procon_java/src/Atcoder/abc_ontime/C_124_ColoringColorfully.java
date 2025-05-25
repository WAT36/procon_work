package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_124_ColoringColorfully {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine();

		int blackstartcount = 0;
		int whitestartcount = 0;

		for(int i=0;i<s.length();i++) {
			char si = s.charAt(i);

			if(i%2 == 0) {
				blackstartcount += (si == '0') ? 1 : 0;
				whitestartcount += (si == '1') ? 1 : 0;
			}else {
				blackstartcount += (si == '1') ? 1 : 0;
				whitestartcount += (si == '0') ? 1 : 0;
			}
		}

		System.out.println(Math.min(blackstartcount, whitestartcount));
	}

}
