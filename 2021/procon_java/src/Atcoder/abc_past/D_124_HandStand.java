package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class D_124_HandStand {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		sc.nextLine();

		String S = sc.nextLine();

		List<Integer> s = new ArrayList<>();

		s.add(0);
		s.add(0);
		char c = S.charAt(0);
		if(S.charAt(0) == '1') {
			s.add(0);
		}
		int tmp = 1;
		for(int i=0;i<S.length()-1;i++) {
			if(S.charAt(i) != S.charAt(i+1)) {
				s.add(tmp);
				tmp = 1;
			}else {
				tmp++;
			}
		}

		if(S.charAt(S.length() - 1) == '0') {
			s.add(tmp);
			s.add(0);
		}else {
			s.add(tmp);
		}

		s.add(0);
		s.add(0);

		for(int i=0;i<K;i++) {
//			System.out.println("s:"+s.toString());
			List<Integer> hsh = new ArrayList<>();
			for(int j=1;j<s.size()-1;j+=2) {
				hsh.add(s.get(j) + s.get(j+1) + s.get(j+2));
			}
//			System.out.println("hsh:"+hsh.toString());
			int max = Collections.max(hsh);
			int maxind = hsh.indexOf(max);
			s.set((maxind * 2)+1, max);
			s.remove((maxind * 2) + 2);
			s.remove((maxind * 2) + 2);

//			System.out.println("s:"+s.toString());
		}

		System.out.println(Collections.max(s));
	}
}
