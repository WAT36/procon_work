package Atcoder.abc_past;

import java.util.Scanner;

public class C_056_GoHome {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int X = sc.nextInt();

		int i=0;
		while(true) {
			if(X <= i*(i+1)/2) {
				break;
			}else {
				i++;
			}
		}
		System.out.println(i);
	}
}
