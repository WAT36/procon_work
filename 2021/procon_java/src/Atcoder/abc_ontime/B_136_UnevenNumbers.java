package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_136_UnevenNumbers {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N =sc.nextInt();

		switch(String.valueOf(N).length()) {
		case 1:
			System.out.println(N);
			break;
		case 2:
			System.out.println(9);
			break;
		case 3:
			System.out.println(9 + (N - 100) + 1);
			break;
		case 4:
			System.out.println(909);
			break;
		case 5:
			System.out.println(909 + (N - 10000) + 1);
			break;
		default:
			System.out.println(90909);
			break;
		}
	}

}
