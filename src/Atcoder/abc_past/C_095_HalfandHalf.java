package Atcoder.abc_past;

import java.util.Scanner;

public class C_095_HalfandHalf {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int X = sc.nextInt();
		int Y = sc.nextInt();

		if(A+B < 2*C) {
			System.out.println((A*X)+(B*Y));
		}else {
			int ans = 0;

			ans += Math.min(X, Y) * (2*C);

			int price = 0;
			if(X>Y) price = A;
			else price = B;

			ans += Math.min(price, 2*C) * Math.abs(X-Y);
			System.out.println(ans);
		}
	}

}
