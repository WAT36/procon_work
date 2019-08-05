package Atcoder.abc_past;

import java.util.Scanner;

public class B_111_ABC111 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int t = (N-1) / 111;
		System.out.println(111*(t+1));
	}
}
