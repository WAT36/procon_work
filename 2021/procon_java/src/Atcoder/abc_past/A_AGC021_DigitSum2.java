package Atcoder.abc_past;

import java.util.Scanner;

public class A_AGC021_DigitSum2 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();

		if(N < 9) {
			System.out.println(N);
		}else {
			long temp = N+1;
			int digit = String.valueOf(temp).length();
			int maxdigit = Integer.parseInt((String.valueOf(temp).substring(0,1)));
			System.out.println(maxdigit + (9*digit - 10));
		}
	}
}
