//台湾旅行中(Day 1)
package Atcoder.abc_past;

import java.util.Scanner;

public class A_125_BiscuitGenerator {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int T = sc.nextInt();

		System.out.println( ((int)(T+0.5)/A) * B);
	}

}
