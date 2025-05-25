package Atcoder.abc_past;

import java.util.Scanner;

public class C_085_Otoshidama {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int Y = sc.nextInt();

		for(int i=0;i<=N;i++) {
			for(int j=0;j<=N-i;j++) {
				int k = N-i-j;
				int yen = (10000 * i) + (5000 * j) + (1000 * k);
				if(yen == Y) {
					System.out.println(i+" "+j+" "+k);
					return;
				}
			}
		}
		System.out.println("-1 -1 -1");
	}
}
