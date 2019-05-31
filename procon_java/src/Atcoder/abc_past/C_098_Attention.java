package Atcoder.abc_past;

import java.util.Scanner;

public class C_098_Attention {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		sc.nextLine();
		String S = sc.nextLine();

		int left_w = 0;
		int left_e = 0;
		int right_w = 0;
		int right_e = 0;

		for (int i = 0; i < N; i++) {
			if (S.charAt(i) == 'W') {
				right_w++;
			} else {
				right_e++;
			}
		}

		int ans = Integer.MAX_VALUE;

		for (int i = 0; i < N; i++) {
			char c = S.charAt(i);

			int turn = 0;
			
			if (c == 'W')
				right_w--;
			else
				right_e--;

			turn = right_e + left_w;
			if (ans > turn) {
				ans = turn;
			}
			
			if (c == 'W')
				left_w++;
			else
				left_e++;

		}
		
		System.out.println(ans);
	}

}
