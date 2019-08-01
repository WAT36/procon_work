package Atcoder.abc_past;

import java.util.Scanner;

public class A_AGC003_Wannagobackhome {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();

		int n = 0;
		int e = 0;
		int w = 0;
		int s = 0;

		for(int i=0;i<S.length();i++) {
			switch(S.charAt(i)) {
			case 'N':
				n++;
				break;
			case 'E':
				e++;
				break;
			case 'W':
				w++;
				break;
			case 'S':
				s++;
				break;
			default:
				break;
			}
		}

		boolean ns = false;
		boolean ew = false;

		if((n==0 && s==0) || (n>=1 && s>=1)) ns = true;
		if((e==0 && w==0) || (e>=1 && w>=1)) ew = true;

		if(ns && ew) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}

}
