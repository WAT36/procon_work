package Atcoder.abc_past;

import java.util.Scanner;

public class B_053_AtoZString {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		int a = 0;
		int z = 0;
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i) == 'A') {
				a = i;
				break;
			}
		}

		for(int i=s.length()-1;i>=0;i--) {
			if(s.charAt(i) == 'Z') {
				z = i;
				break;
			}
		}

		System.out.println(z-a+1);
	}

}
