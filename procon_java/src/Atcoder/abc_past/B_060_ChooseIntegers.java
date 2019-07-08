package Atcoder.abc_past;

import java.util.Scanner;

public class B_060_ChooseIntegers {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();

		int mod;
		int i;
		if(A >= C) {
			mod = (A-C)%B;
			i=2;
		}else {
			mod = (((C/A) + 1)*A - C)%B;
			i = ((C/A) + 2);
		}
		int mod_i = -1;
		while(mod != mod_i) {
			mod_i = (A*i - C)%B;
			if(mod_i == 0) {
				System.out.println("YES");
				return;
			}else {
				i++;
			}
		}
		System.out.println("NO");
	}

}
