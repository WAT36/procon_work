package Atcoder.abc_past;

import java.util.Scanner;

public class C_099_StrangeBank {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int ans = 0;

		while (N >= 6) {
			int x = (int) (Math.log(N) / Math.log(9));
			int y = (int) (Math.log(N) / Math.log(6));
			x = (int) Math.pow(9, x);
			y = (int) Math.pow(6, y);
			if(x == 0 && y == 0) {
				break;
			}else if(x > y) {
				N -= x;
				ans++;
			}else {
				N -= y;
				ans++;
			}
		}

		ans += N;

		System.out.println(ans);
	}
}
