package Atcoder.abc_past;

import java.util.Scanner;

public class C_103_ModuleSimulation {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		int[] a = new int[N];
		long lcm_a = 1;
		for(int i=0;i<N;i++) {
			a[i] = sc.nextInt();
			lcm_a = lcm(lcm_a,a[i]);
		}

		long m = lcm_a - 1;

		long ans=0;
		long ans2=0;
		for(int i=0;i<N;i++) {
			ans += a[i];
		}

		System.out.println(ans - N);
	}

	//最小公倍数
	public static long lcm (long lcm_a, long b) {
			long temp;
			long c = lcm_a;
			c *= b;
			while((temp = lcm_a%b)!=0) {
				lcm_a = b;
				b = temp;
			}
			return c/b;
	}

}
