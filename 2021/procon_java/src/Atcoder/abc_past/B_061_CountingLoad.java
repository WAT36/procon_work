package Atcoder.abc_past;

import java.util.Scanner;

public class B_061_CountingLoad {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[] loads = new int[N+1];
		for(int i=0;i<M;i++) {
			int a = sc.nextInt();
			loads[a]++;
			int b = sc.nextInt();
			loads[b]++;
		}

		for(int i=1;i<=N;i++) {
			System.out.println(loads[i]);
		}
	}

}
