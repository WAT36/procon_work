package Atcoder.corporate;

import java.util.Scanner;

public class C_Tenka1 {

	public static final long MAX = 3500;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();

		for(long h=1;h<=MAX;h++) {
			for(long n=1;n<=MAX;n++) {
				long child = N*h*n;
				long mother = 4*h*n - N*n - N*h;

				if(mother != 0 && child%mother == 0 && child/mother > 0) {
					System.out.println(h + " " + n + " " + (child/mother));
					return;
				}

			}
		}
	}
}
