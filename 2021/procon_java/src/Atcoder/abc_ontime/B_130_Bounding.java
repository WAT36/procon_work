package Atcoder.abc_ontime;

import java.util.Arrays;
import java.util.Scanner;

public class B_130_Bounding {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int X = sc.nextInt();

		int[] D = new int[N+1];
		int[] L = new int[N+1];
		D[0] = 0;
		for(int i=0;i<N;i++) {
			L[i] = sc.nextInt();
			D[i+1] = D[i] + L[i];
		}
		Arrays.sort(D);

		int ans = 0;
		for(int i=0;i<N+1;i++) {
			if(D[i] > X) {
				System.out.println(ans);
				return;
			}else {
				ans++;
			}
		}
		System.out.println(ans);
	}
}
