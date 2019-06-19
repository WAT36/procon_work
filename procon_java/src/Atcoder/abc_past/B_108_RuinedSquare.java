package Atcoder.abc_past;

import java.util.Scanner;

public class B_108_RuinedSquare {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int x1 = sc.nextInt();
		int y1 = sc.nextInt();
		int x2 = sc.nextInt();
		int y2 = sc.nextInt();

		int[] vector = new int[2];
		vector[0] = x2 - x1;
		vector[1] = y2 - y1;

		int swap = vector[0];
		vector[0] = -1 * vector[1];
		vector[1] = swap;

		int x3 = x2 + vector[0];
		int y3 = y2 + vector[1];

		swap = vector[0];
		vector[0] = -1 * vector[1];
		vector[1] = swap;

		int x4 = x3 + vector[0];
		int y4 = y3 + vector[1];

		System.out.println(x3+" "+y3+" "+x4+" "+y4);
	}

}
