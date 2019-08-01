package Atcoder.corporate;

import java.util.Scanner;

public class C_CODEFESTIVAL2017_qualC {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		long sum = (long) Math.pow(3, N);
		long odd = 1;

		for(int i=0;i<N;i++) {
			int a = sc.nextInt();

			if(a % 2 == 0) {
				odd *= 2;
			}
		}

		System.out.println(sum - odd);
	}

}
