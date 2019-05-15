package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_121_solve {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		int C = sc.nextInt();

		int[] B = new int[M];
		for(int i=0;i<M;i++) {
			B[i] = sc.nextInt();
		}

		int count = 0;
		int sum = 0;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				sum += B[j] * sc.nextInt();
			}
			sum += C;

			if(sum > 0) {
				count++;
			}

			sum = 0;
		}

		System.out.println(count);
	}

}
