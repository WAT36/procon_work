package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_097_KthSubstring {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine();
		int K = sc.nextInt();

		List<String> sub = new ArrayList<>();
		char fast_char = 'z';

		for(int i=0;i<s.length();i++) {
			if(s.charAt(i) <= fast_char) {
				fast_char = s.charAt(i);
			}else if(sub.size() > K) {
				continue;
			}

			for(int j=i;j<=Math.min(s.length(),i+5);j++) {
				String temp = s.substring(i, j);
				if(!sub.contains(temp)) {
					sub.add(temp);
				}
			}
		}

		Collections.sort(sub);

		System.out.println(sub.get(K));
	}
}
