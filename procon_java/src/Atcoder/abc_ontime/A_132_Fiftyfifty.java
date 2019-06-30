package Atcoder.abc_ontime;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class A_132_Fiftyfifty {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		Map<String,Integer> si = new HashMap<String,Integer>();
		for(int i=0;i<s.length();i++) {
			String temp = s.substring(i, i+1);
			if(si.containsKey(temp)) {
				int t = si.get(temp);
				if(t == 2) {
					System.out.println("No");
					return;
				}
				t++;
				si.put(temp, t);
			}else {
				si.put(temp, 1);
			}
		}

		if(si.size() != 2) {
			System.out.println("No");
		}else {
			System.out.println("Yes");
		}
	}
}
