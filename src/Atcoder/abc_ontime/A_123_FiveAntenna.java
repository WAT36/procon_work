package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_123_FiveAntenna {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int[] antenna = new int[5];

		for (int i = 0; i < 5; i++) {
			antenna[i] = sc.nextInt();
		}

		int k = sc.nextInt();

		if (antenna[4] - antenna[0] > k) {
			System.out.println(":(");
		} else {
			System.out.println("Yay!");
		}
	}

}
