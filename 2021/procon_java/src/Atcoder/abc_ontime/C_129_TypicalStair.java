package Atcoder.abc_ontime;

import java.util.Scanner;

public class C_129_TypicalStair {

	public static final long MOD = 1000000007L;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		long[] a = new long[M];
		long[] steps = new long[N+1];
		for(int i=0;i<N;i++) {
			steps[i] = 0;
		}

		for(int i=0;i<M;i++) {
			a[i] = sc.nextLong();
			steps[(int) a[i]] = -1;
		}

		steps[0] = 1;
		steps[1] = (steps[1] == -1) ? -1 : 1;
		for(int i=2;i<N+1;i++) {

			if(steps[i] == -1) continue;

			if(steps[i-1] == -1 && steps[i-2] == -1) {
				System.out.println(0);
				return;
			}

			if(steps[i-1] == -1) {
				steps[i] = steps[i-2];
			}else if(steps[i-2] == -1) {
				steps[i] = steps[i-1];
			}else {
				steps[i] = (steps[i-1] + steps[i-2])%MOD;
			}
		}
		System.out.println(steps[N]%MOD);
	}
}
