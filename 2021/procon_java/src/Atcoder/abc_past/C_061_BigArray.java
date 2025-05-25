package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class C_061_BigArray {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long K = sc.nextLong();

		int[][] iab = new int[N][3];
		for(int i=0;i<N;i++) {
			iab[i][0] = i;
			iab[i][1] = sc.nextInt();
			iab[i][2] = sc.nextInt();
		}
		Arrays.sort(iab, (a,b)->Integer.compare(a[1], b[1]));
		long sum = 0;
		for(int i=0;i<N;i++) {
			sum += iab[i][2];
			if(sum >= K) {
				System.out.println(iab[i][1]);
				return;
			}
		}
	}
}
