package Atcoder.abc_past;

import java.util.Scanner;

public class B_066_ss {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		int l = s.length();
		for(int i=l-2;i>1;i-=2) {
			String a = s.substring(0, i/2);
			String b = s.substring(i/2, i);
			if(a.equals(b)) {
				System.out.println(i);
				return;
			}
		}
	}

}
