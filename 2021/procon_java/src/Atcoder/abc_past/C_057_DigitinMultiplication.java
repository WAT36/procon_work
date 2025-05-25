package Atcoder.abc_past;

import java.util.Scanner;

public class C_057_DigitinMultiplication {

	public static void main(String args[]){

		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();

		long M = (long) Math.ceil(Math.sqrt(N));

		int ans = Integer.MAX_VALUE;
		for(long i=M;i>0;i--) {
			if(N%i == 0) {
				int f = Math.max(String.valueOf(i).length(),String.valueOf(N/i).length());
				if(ans > f) {
					ans = f;
				}
			}
		}
		System.out.println(ans);
	}
}
