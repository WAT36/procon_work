package Atcoder.abc_past;

import java.util.Scanner;

public class C_096_GridRepaint {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int H = sc.nextInt();
		int W = sc.nextInt();
		sc.nextLine();

		String[] s = new String[H];
		for(int i=0;i<H;i++) {
			s[i] = sc.nextLine();
		}

		for(int i=0;i<H;i++) {
			for(int j=0;j<W;j++) {

				if(s[i].charAt(j) == '#') {

					if( (i > 0 && s[i-1].charAt(j) == '.') &&
						(i < H-1 && s[i+1].charAt(j) == '.') &&
						(j > 0 && s[i].charAt(j-1) == '.') &&
						(j < W-1 && s[i].charAt(j+1) == '.')) {

						System.out.println("No");
						return;
					}
				}
			}
		}

		System.out.println("Yes");
	}

}
