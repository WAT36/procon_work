package Atcoder.abc_past;

import java.util.Scanner;

public class C_ARC080_4adjacent {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int odd = 0;
		int two_x = 0;
		int four_x = 0;

		for(int i=0;i<N;i++) {
			int a = sc.nextInt();
			if(a % 2 == 1) {
				odd++;
			}else if(a % 4 == 0) {
				four_x++;
			}else {
				two_x++;
			}
		}

		if(odd - 1 > four_x) {
			System.out.println("No");
		}else if(odd - 1 == four_x) {
			if(two_x == 0) {
				System.out.println("Yes");
			}else {
				System.out.println("No");
			}
		}else {
			System.out.println("Yes");
		}
	}

}
