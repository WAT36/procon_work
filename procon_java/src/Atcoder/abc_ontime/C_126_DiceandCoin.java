package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_126_DiceandCoin {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();

		double p = 0;

		for(int i=1;i<=N;i++) {
			double pi = 1;
			int temp = i;
			while(temp < K) {
				pi /= 2;
				temp *= 2;
			}
			p += pi;
		}
		p /= N;
		System.out.println(p);
	}

	public static boolean ispow2(int a) {
		int x = a & (a-1);
		if(x == 0) {
			return true;
		}else {
			return false;
		}
	}

	public static double log2(double a) {
		return Math.log(a)/Math.log(2);
	}
}
