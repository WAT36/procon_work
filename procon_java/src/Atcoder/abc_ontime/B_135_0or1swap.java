package Atcoder.abc_ontime;

import java.util.Arrays;
import java.util.Scanner;

public class B_135_0or1swap {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] p = new int[N];
		for(int i=0;i<N;i++) {
			p[i] = sc.nextInt();
		}

		int[] sorted_p = p.clone();
		Arrays.sort(p);

		int diff = 0;
		for(int i=0;i<N;i++) {
			if(p[i] != sorted_p[i]) {
				diff++;
			}

			if(diff > 2) {
				System.out.println("NO");
				return;
			}
		}
		System.out.println("YES");
	}

}
