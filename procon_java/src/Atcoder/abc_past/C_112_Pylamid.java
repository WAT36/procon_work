package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class C_112_Pylamid {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] xyh = new int[N][3];

		for(int i=0;i<N;i++) {
			xyh[i][0] = sc.nextInt();
			xyh[i][1] = sc.nextInt();
			xyh[i][2] = sc.nextInt();
		}

		Arrays.sort(xyh, (a,b)->Integer.compare(b[2], a[2]));
		if(xyh[0][2] == 0) {
			System.out.println("7 7 1");
			return;
		}

		boolean flag = true;
		for(int i=0;i<=100;i++) {
			for(int j=0;j<=100;j++) {
				int h = 0;
				for(int k=0;k<N;k++) {
					if(h == 0) {
						if(xyh[k][2] == 0) {
							continue;
						}else {
							h = xyh[k][2] + Math.abs(xyh[k][0] - i) + Math.abs(xyh[k][1] - j);
						}
					}

					int hk = Math.max(0, h - Math.abs(xyh[k][0] - i) - Math.abs(xyh[k][1] - j));
					if(xyh[k][2] != hk) {
						flag = false;
						break;
					}
				}

				if(flag) {
					System.out.println(i + " " + j + " " + h);
					return;
				}else {
					flag = true;
				}
			}
		}
	}

}
