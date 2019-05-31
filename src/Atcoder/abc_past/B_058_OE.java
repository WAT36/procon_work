package Atcoder.abc_past;

import java.util.Scanner;

public class B_058_OE {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String O = sc.nextLine();
		String E = sc.nextLine();
		int l = Math.min(O.length(), E.length());

		String pass = "";
		for(int i=0;i<l;i++) {
			pass = pass + O.substring(i, i+1);
			pass = pass + E.substring(i, i+1);
		}

		if(O.length() != E.length()) {
			pass = pass + O.substring(O.length()-1);
		}

		System.out.println(pass);
	}
}
