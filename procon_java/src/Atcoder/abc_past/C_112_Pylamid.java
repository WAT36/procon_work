package Atcoder.abc_past;

import java.util.Scanner;

public class C_112_Pylamid {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[][] xyh = new int[N][3];
		for (int i = 0; i < N; i++) {
			xyh[i] = new int[] { sc.nextInt(), sc.nextInt(), sc.nextInt() };
		}

		int p;
		for (p = 0; p < N; p++) {
			if (xyh[p][2] > 0) {
				break;
			}
		}

		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				next: {
					int H = xyh[p][2] - Math.abs(xyh[p][0] - i) - Math.abs(xyh[p][1] - j);

					for (int k = 0; k < N; k++) {
						int hk = xyh[k][2] + Math.abs(xyh[k][0] - i) + Math.abs(xyh[k][1] - j);

						if (H != hk && xyh[k][2] > 0) {
							break next;
						}
						else if(H > hk && xyh[k][2] <= 0) {
							break next;
						}
					}
					System.out.println(i+" "+j+" "+H);
					return;
				}
			}
		}
	}

}
