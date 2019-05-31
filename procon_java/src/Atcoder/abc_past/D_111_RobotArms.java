package Atcoder.abc_past;

import java.util.Scanner;

public class D_111_RobotArms {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] u = new int[N];
		int[] v = new int[N];
		for(int i=0;i<N;i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			u[i] = x+y;
			v[i] = x-y;
		}

		int temp = u[0] % 2;
		for(int i=1;i<N-1;i++) {
			if(temp != (u[i] % 2)) {
				System.out.println("-1");
				return;
			}
		}

	}
}
