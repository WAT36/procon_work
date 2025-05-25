package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class A_AGC027_CandyDistributionAgain {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long x = sc.nextLong();
		long[] a = new long[N];
		long sum = 0;
		for(int i=0;i<N;i++) {
			a[i] = sc.nextLong();
			sum += a[i];
		}
		Arrays.sort(a);

		if(sum < x) {
			System.out.println(N-1);
		}else if(sum == x) {
			System.out.println(N);
		}else {
			long asum = 0;
			for(int i=0;i<N;i++) {
				asum += a[i];
				if(asum > x) {
					System.out.println(i);
					break;
				}
			}
		}
	}
}