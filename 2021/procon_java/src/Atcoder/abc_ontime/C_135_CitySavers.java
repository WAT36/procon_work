package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_135_CitySavers {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] a = new int[N+1];
		int[] b = new int[N];

		for(int i=0;i<N+1;i++) {
			a[i] = sc.nextInt();
		}

		for(int i=0;i<N;i++) {
			b[i] = sc.nextInt();
		}

		long ans = 0;
		for(int i=0;i<N;i++) {

			if(a[i] >= b[i]) {
				a[i] -= b[i];
				ans += b[i];
			}else {
				b[i] -= a[i];
				ans  += a[i];
				a[i] -= a[i];

				if(a[i+1] >= b[i]) {
					a[i+1] -= b[i];
					ans += b[i];
				}else {
					ans += a[i+1];
					a[i+1] -= a[i+1];
				}
			}
		}
		System.out.println(ans);
	}

}
