package Atcoder.abc_past;

import java.util.Scanner;

public class B_097_Exponential {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int X =sc.nextInt();

		for(int i=X;i>0;i--) {

			if(i == 1) {
				System.out.println(1);
				return;
			}

			for(int b=(int)Math.sqrt(i)+1;b>2;b--) {
				int temp = i;
				int p = 0;
				System.out.println(i+","+b);
				while(temp % b == 0) {
					p++;
					temp /= b;
				}

				if(temp == 1 && p > 1) {
					System.out.println(i);
					return;
				}
			}
		}
	}
}
