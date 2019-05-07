package Atcoder.abc_past;

import java.util.Scanner;

public class C_101_Minimization {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		sc.nextLine();
		sc.nextLine();

		int i = 1;
		while( N > (i * K) - (i - 1)) {
			i++;
		}

		System.out.println(i);
	}

}
