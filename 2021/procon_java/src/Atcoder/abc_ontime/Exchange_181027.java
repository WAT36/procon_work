package Atcoder.abc_ontime;

import java.util.Scanner;

public class Exchange_181027 {

	public static int[] exchange(int a,int b) {

		int swap = 0;

		if(a % 2 != 0) {
			a--;
		}

		swap = a/2;
		a /= 2;
		b += swap;
		return new int[] {a,b};
	}

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		String[] n = s.split(" ");

		int a = Integer.parseInt(n[0]);
		int b = Integer.parseInt(n[1]);
		int k = Integer.parseInt(n[2]);


		int count = 0;
		int[] swap;
		while(count < k) {

			if(count % 2 == 0) {
				swap = exchange(a,b);
				a = swap[0];
				b = swap[1];
			}else {
				swap = exchange(b,a);
				b = swap[0];
				a = swap[1];
			}

			count++;
		}

		System.out.println(a + " " + b);
	}
}
