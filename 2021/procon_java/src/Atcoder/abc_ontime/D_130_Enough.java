package Atcoder.abc_ontime;

import java.util.Scanner;

public class D_130_Enough {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		long K = sc.nextLong();

		long[] a = new long[N];
		for(int i=0;i<N;i++) {
			a[i] = sc.nextLong();
		}

		long ans = 0;
		int starti = 0;
		long sum = 0;
		for(int i=0;i<N;i++) {
			for(int j=starti;j<N;j++) {
				sum += a[j];
//				System.out.println("i:"+i+", j:"+j+", sum:"+sum+", ans:"+ans);
				if(sum >= K) {
//					System.out.println("K>!");
					ans += (N-1)-j+1;
					starti = j;
					break;
				}
				starti = j;
			}
			sum -= a[i];
			sum -= a[starti];
		}
		System.out.println(ans);
	}
}
