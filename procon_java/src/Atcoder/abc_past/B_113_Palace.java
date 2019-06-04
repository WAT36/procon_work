package Atcoder.abc_past;

import java.util.Scanner;

public class B_113_Palace {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int T = sc.nextInt();
		int A = sc.nextInt();
		int[] H = new int[N];

		int near_i = 0;
		double temp = 0;
		double near_t = Integer.MAX_VALUE;
		for(int i=0;i<N;i++) {
			H[i] = sc.nextInt();
			temp = T - (H[i] * 0.006);

			if(Math.abs(temp - A) < Math.abs(near_t - A)) {
				near_t = temp;
				near_i = i;
			}
		}
		System.out.println(near_i+1);
	}
}
