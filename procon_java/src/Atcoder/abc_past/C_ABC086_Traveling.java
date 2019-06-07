package Atcoder.abc_past;

import java.util.Scanner;

public class C_ABC086_Traveling {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int temp = 0;
		int[] t = new int[N+1];
		int[] x = new int[N+1];
		int[] y = new int[N+1];

		t[0] = 0;
		x[0] = 0;
		y[0] = 0;

		for(int i=1;i<N+1;i++) {
			t[i] = sc.nextInt();
			x[i] = sc.nextInt();
			y[i] = sc.nextInt();
		}

		for(int i=1;i<N+1;i++) {
			temp = t[i] - t[i-1];
			int d = Math.abs(x[i] - x[i-1]) + Math.abs(y[i] - y[i-1]);

			if(d > temp) {
				System.out.println("No");
				return;
			}else if((temp - d)%2 != 0) {
				System.out.println("No");
				return;
			}
		}

		System.out.println("Yes");
	}

}
