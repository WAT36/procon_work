package Atcoder.abc_past;

import java.util.Scanner;

public class C_088_TakahashisInformation {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int[][] c = new int[3][3];

		int csum = 0;
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				c[i][j] = sc.nextInt();
				csum += c[i][j];
			}
		}

		int[] threesum = new int[6];
		threesum[0] = c[0][0] + c[1][1] + c[2][2];
		threesum[1] = c[0][0] + c[2][1] + c[1][2];
		threesum[2] = c[1][0] + c[0][1] + c[2][2];
		threesum[3] = c[1][0] + c[2][1] + c[0][2];
		threesum[4] = c[2][0] + c[1][1] + c[0][2];
		threesum[5] = c[2][0] + c[0][1] + c[1][2];
		for(int i=1;i<6;i++) {
			if(threesum[0] != threesum[i]) {
				System.out.println("No");
				return;
			}
		}
		System.out.println("Yes");

	}
}
