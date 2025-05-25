package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class C_111_slashslash {

	public static final int N = 100000;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[][] even = new int[N+1][2];
		int[][] odd = new int[N+1][2];
		for(int i=1;i<=n;i++) {
			int v = sc.nextInt();
			if(i%2 == 0) {
				even[v][0] = v;
				even[v][1]++;
			}else {
				odd[v][0] = v;
				odd[v][1]++;
			}
		}
		Arrays.sort(even,(a,b)->Integer.compare(b[1], a[1]));
		Arrays.sort(odd,(a,b)->Integer.compare(b[1], a[1]));
		if(even[0][0] != odd[0][0]) {
			System.out.println(((n/2) + (n%2) - odd[0][1]) + ((n/2) - even[0][1]));
		}else {
			if(odd[0][1] + even[1][1] > odd[1][1] + even[0][1]) {
				System.out.println(((n/2) + (n%2) - odd[0][1]) + ((n/2) - even[1][1]));
			}else {
				System.out.println(((n/2) + (n%2) - odd[1][1]) + ((n/2) - even[0][1]));
			}
		}
	}

}