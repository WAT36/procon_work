package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class C_ABC047_1DRevarsi {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		String S = sc.nextLine();

		char c = S.charAt(0);
		int N = S.length();
		List<Integer> bw = new ArrayList<>();
		int temp=0;
		for(int i=0;i<N;i++) {
			if(c == S.charAt(i)) {
				temp++;
			}else {
				bw.add(temp);
				temp=1;
				c = S.charAt(i);
			}
		}
		bw.add(temp);

		System.out.println(bw.size()-1);
	}
}
