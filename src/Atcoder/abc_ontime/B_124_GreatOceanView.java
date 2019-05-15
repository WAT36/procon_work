package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_124_GreatOceanView {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		int[] x = new int[N];
		for(int i = 0;i<N;i++) {
			x[i] = sc.nextInt();
		}

		int count = 0,max = 0;
		for(int i=0;i<N;i++) {
			if(x[i] >= max) {
				max = x[i];
				count++;
			}
		}
		System.out.println(count);
	}

}
