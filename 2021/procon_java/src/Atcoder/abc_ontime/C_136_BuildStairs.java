package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_136_BuildStairs {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[] H = new int[N];
		int max_h = 0;
		for(int i=0;i<N;i++) {
			H[i] = sc.nextInt();

			if(H[i] > max_h) {
				max_h = H[i];
			}

			if(max_h - H[i] > 1) {
				System.out.println("No");
				return;
			}
		}
		System.out.println("Yes");
	}
}
