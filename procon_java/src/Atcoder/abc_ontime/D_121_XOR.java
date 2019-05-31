package Atcoder.abc_ontime;

import java.util.Scanner;

public class D_121_XOR {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		long A = sc.nextLong();
		long B = sc.nextLong();

		int ans = (int)(B%4);

		long ansa = A;
		System.out.println(A);
		for(long i=A+1;i<=B;i++) {
			ansa = ansa^i;
			System.out.println(ansa);
		}
//		if(A==B) {
//			System.out.println(B);
//		}else if((int)(B-A) == 1) {
//			System.out.println(A^B);
//		}else {
//			switch(ans) {
//			case 0:
//				System.out.println(B + 1);
//				break;
//			case 1:
//				System.out.println(0);
//				break;
//			case 2:
//				System.out.println(B);
//				break;
//			case 3:
//				System.out.println(1);
//				break;
//			}
//		}
	}
}
