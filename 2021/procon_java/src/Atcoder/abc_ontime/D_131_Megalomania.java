package Atcoder.abc_ontime;

import java.util.Arrays;
import java.util.Scanner;

public class D_131_Megalomania {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N =sc.nextInt();
		int[][] ab = new int[N][2];

		for(int i=0;i<N;i++) {
			ab[i][0] = sc.nextInt();
			ab[i][1] = sc.nextInt();
		}
		Arrays.sort(ab, (a,b)->Integer.compare(a[1], b[1]));

		int asum = 0;
		int b = 0;
		for(int i=0;i<N;i++) {
			asum += ab[i][0];
			b = ab[i][1];
			if(asum > b) {
				System.out.println("No");
				return;
			}
		}
		System.out.println("Yes");
	}
}
