package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class B_071_NotFound {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();

		List<Character> c = new ArrayList<>();
		for(int i=0;i<S.length();i++) {
			if(!c.contains(S.charAt(i))) c.add(S.charAt(i));
		}
		Collections.sort(c);

		char x = 'a';
		int i=0;
		while(x <= 'z') {
			if(i >= c.size()) {
				break;
			}if(x == c.get(i)) {
				x++;
				i++;
			}else {
				break;
			}
		}

		if(x > 'z') {
			System.out.println("None");
		}else {
			System.out.println(x);
		}
	}
}