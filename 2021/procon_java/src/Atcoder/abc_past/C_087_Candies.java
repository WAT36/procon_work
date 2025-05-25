package Atcoder.abc_past;

import java.util.Scanner;

public class C_087_Candies {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] a1 = new int[N];
		int[] a2 = new int[N];

		for(int i=0;i<N;i++) {
			a1[i] = sc.nextInt();
		}

		int suma2 = 0;
		for(int i=0;i<N;i++) {
			a2[i] = sc.nextInt();
			suma2 += a2[i];
		}

		int suma1 = a1[0];
		int maxsum = suma1 + suma2;
		for(int i=1;i<N;i++) {
			suma1 += a1[i];
			suma2 -= a2[i-1];
			if(maxsum < (suma1 + suma2)) {
				maxsum = (suma1 + suma2);
			}
		}
		System.out.println(maxsum);
	}

}
