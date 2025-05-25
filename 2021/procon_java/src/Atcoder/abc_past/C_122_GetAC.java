package Atcoder.abc_past;

import java.util.Scanner;

public class C_122_GetAC {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int Q = sc.nextInt();
		String S = sc.next();

		int[] accum = new int[N];
		boolean flag = false;
		if(S.charAt(0) == 'A') flag = true;

		for(int i=1;i<N;i++) {
			if(S.charAt(i) == 'A') {
				flag = true;
				accum[i] = accum[i-1];
			}else if(S.charAt(i) == 'C') {
				if(flag) {
					flag = false;
					accum[i] = accum[i-1] + 1;
				}else {
					accum[i] = accum[i-1];
				}
			}else {
				if(flag) flag = false;
				accum[i] = accum[i-1];
			}
		}

		int[] ans = new int[Q];
		for(int i=0;i<Q;i++) {
			int l = sc.nextInt();
			int r = sc.nextInt();
			ans[i] = accum[r-1] - accum[l-1];
		}

		for(int i=0;i<Q;i++) {
			System.out.println(ans[i]);
		}
	}
}
