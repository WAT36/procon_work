package Atcoder.abc_past;

import java.util.Scanner;

public class B_102_MaximumDifference {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int max = 0;
		int min = Integer.MAX_VALUE;
		for(int i=0;i<N;i++) {
			int A = (int)Math.abs(sc.nextInt());
			if(max < A) max = A;
			if(min > A) min = A;
		}

		System.out.println(max - min);
	}

}
