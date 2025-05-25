package Atcoder.abc_past;

import java.util.Scanner;

public class C_125_GCDonBlackboard {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] a = new int[N+1];
		int[] gcd_order = new int[N+2];
		int[] gcd_reverse = new int[N+2];

		// 1~N
		gcd_order[0] = 0;
		int max_gcd = 0;
		for(int i=1;i<N+1;i++) {
			a[i] = sc.nextInt();
			gcd_order[i] = gcd(a[i],gcd_order[i-1]);
		}

		gcd_reverse[N+1] = 0;
		gcd_reverse[N] = gcd(a[N],0);
		max_gcd = gcd_order[N];

		for(int i=N-1;i>=0;i--) {
			gcd_reverse[i] = gcd(a[i],gcd_reverse[i+1]);
			int gcd = gcd(gcd_order[i], gcd_reverse[i+2]);
			max_gcd = Math.max(max_gcd, gcd);
		}

		System.out.println((int)max_gcd);
	}

	//整数a,bの最大公約数
	public static int gcd(int a,int b) {
		if(b == 0) return a;
		else return gcd(b,a%b);
	}

}
