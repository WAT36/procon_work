package Atcoder.abc_past;

import java.util.Scanner;

public class C_076_DubiousDocument2 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String Sdash = sc.nextLine();
		String T = sc.nextLine();

		String ans = "zzzzzzz";
		for(int i=0;i<=Sdash.length() - T.length();i++) {
			String temp = Sdash;
			int k = i;
			boolean flag = true;
			for(int j=0;j<T.length();j++) {
				System.out.println("i:"+i+",j:"+j+",k:"+k+",temp:"+temp);
				if(Sdash.charAt(k) != '?' && T.charAt(j) != Sdash.charAt(k)) {
					flag = false;
					break;
				}else{
					temp = temp.substring(0,k) + T.substring(j, j+1) + temp.substring(k+1, Sdash.length());
					k++;
				}
			}

			if(flag) {
				for(int j=0;j<Sdash.length();j++) {
					if(temp.charAt(j) == '?') {
						temp = temp.substring(0,j) + "a" + temp.substring(j+1,Sdash.length());
					}
				}

				if(ans.compareTo(temp) >= 0) {
					ans = temp;
				}
			}
		}

		if(ans.equals("zzzzzzz")) {
			System.out.println("UNRESTORABLE");
		}else {
			System.out.println(ans);
		}
	}
}
