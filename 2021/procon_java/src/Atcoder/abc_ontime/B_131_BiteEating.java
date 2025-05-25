package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_131_BiteEating {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int L = sc.nextInt();

		int tastesum = N*(L-1) + N*(1+N)/2;

		int mintaste = Integer.MAX_VALUE;
		int mintasteabs = Integer.MAX_VALUE;
		for(int i=1;i<=N;i++) {
			int t = L+i-1;
			if(mintasteabs > Math.abs(t)) {
				mintaste = t;
				mintasteabs = Math.abs(t);
			}
		}
		System.out.println(tastesum - mintaste);
	}
}
