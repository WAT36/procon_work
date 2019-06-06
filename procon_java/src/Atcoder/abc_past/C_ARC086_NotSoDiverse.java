package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class C_ARC086_NotSoDiverse {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();

		int[] A = new int[N];
		int[] num = new int[N];
		for(int i=0;i<N;i++) {
			A[i] = sc.nextInt();
			num[A[i]-1]++;
		}

		Arrays.sort(num);

		int ans = 0;
		for(int i=num.length-1-K;i>=0;i--) {
			ans += num[i];
		}
		System.out.println(ans);
	}

}
