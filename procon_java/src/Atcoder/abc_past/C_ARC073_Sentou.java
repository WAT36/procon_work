package Atcoder.abc_past;

import java.util.Scanner;

public class C_ARC073_Sentou {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int T = sc.nextInt();
		int[] t = new int[N];

		int sum = 0;
		t[0] = sc.nextInt();
		for(int i=1;i<N;i++) {
			t[i] = sc.nextInt();

			if(t[i-1] + T < t[i]) {
				sum += T;
			}else {
				sum += t[i] - t[i-1];
			}
		}

		sum += T;
		System.out.println(sum);
	}
}
