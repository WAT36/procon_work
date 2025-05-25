package Atcoder.abc_past;

import java.util.Scanner;

public class C_106_ToInfinity {

	public static void main(String[] args) {

		final long FIVE_QUADRILION = 5000000000000000L;

		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();
		long K = Long.parseLong(sc.nextLine());

		for(int i=0;i<S.length();i++) {
			int x = Integer.parseInt(S.substring(i, i+1));

			double t = Math.pow(x, FIVE_QUADRILION);

			if( t >= K) {
				System.out.println(x);
				return;
			}else {
				K -= t;
			}
		}
	}
}
