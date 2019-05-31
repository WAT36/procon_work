package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_127_Prison {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		int max_L = 0;
		int min_R = N;

		for(int i=0;i<M;i++) {
			int L = sc.nextInt();
			int R = sc.nextInt();

			if(max_L <= L) {
				max_L = L;
			}

			if(R <= min_R) {
				min_R = R;
			}
		}

		int ans = min_R - max_L + 1;
		if(ans > 0) {
			System.out.println(ans);
		}else {
			System.out.println(0);
		}
	}
}
