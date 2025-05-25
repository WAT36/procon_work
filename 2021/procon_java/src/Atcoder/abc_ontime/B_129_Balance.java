package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_129_Balance {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] W = new int[N];
		int[] accumsum = new int[N];
		int sum = 0;
		for(int i=0;i<N;i++) {
			W[i] = sc.nextInt();
			sum += W[i];
			accumsum[i] = sum;
		}

		int ans = Integer.MAX_VALUE;
		for(int i=0;i<N;i++) {
			int diff = Math.abs(accumsum[i] - (sum - accumsum[i]));
			if(ans > diff) ans = diff;
		}
		System.out.println(ans);
	}
}
