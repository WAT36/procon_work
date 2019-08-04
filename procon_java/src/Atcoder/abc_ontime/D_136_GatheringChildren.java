package Atcoder.abc_ontime;

import java.util.Scanner;

public class D_136_GatheringChildren {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String S = sc.next();

		int r = 0;
		int l = 0;
		for(int i=0;i<S.length()-1;i++) {

			if(S.charAt(i) == 'R') {
				r++;
			}else {
				l++;
			}

			if(i == S.length()-2) l++;

			if((S.charAt(i) == 'L' && S.charAt(i+1) == 'R') || i == S.length()-2) {
				calclist(r,l);
				r=0;
				l=0;
			}
		}


	}

	public static void calclist(int r,int l){

		int left =  (int) Math.ceil((double)r/(double)2) + (int) Math.floor((double)l/(double)2);
		int right = (int) Math.ceil((double)l/(double)2) + (int) Math.floor((double)r/(double)2);
		for(int i=1;i<r;i++) {
			System.out.print(0 + " ");
		}
		System.out.print(left + " ");
		System.out.print(right + " ");
		for(int i=1;i<l;i++) {
			System.out.print(0 + " ");
		}
	}

}
