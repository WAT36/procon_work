package Atcoder.arc_ontime.arc_190508_diverta;

import java.util.Scanner;

public class B_RGBboxed {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int R = sc.nextInt();
		int G = sc.nextInt();
		int B = sc.nextInt();
		int N = sc.nextInt();

		int count=0;

		for(int i=0;(R*i)<=N;i++) {
			for(int j=0;(R*i)+(G*j)<=N;j++) {
				int rest = N - (R*i) - (G*j);

				if(rest % B == 0){
					count++;
				}
			}
		}

		System.out.println(count);
	}

}
