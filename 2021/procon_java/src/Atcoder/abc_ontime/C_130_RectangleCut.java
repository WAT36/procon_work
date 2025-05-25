package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_130_RectangleCut {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int W = sc.nextInt();
		int H = sc.nextInt();
		int x = sc.nextInt();
		int y = sc.nextInt();

		String s = ((double)x == (double)W/(double)2 &&
					(double)y == (double)H/(double)2) ? "1" : "0";
		double area = (double)W*(double)H/2;
		String a = String.format("%.6f", area);
		System.out.println(a+" "+s);
	}
}
