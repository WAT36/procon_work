package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class B_118_foods {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String[] s = sc.nextLine().split(" ");

		int N = Integer.parseInt(s[0]);
		int M = Integer.parseInt(s[1]);

		String [][] tt = new String[N][];
		for(int i=0;i<N;i++) {
			tt[i] = sc.nextLine().split(" ");
		}

		List<String> a = new ArrayList<String>();
		a = Arrays.asList(tt[0]);
		List<String> ans = new ArrayList<>(a);
		ans.remove(0);

		List<String> t = new ArrayList<String>();
		for (int i=1;i<N;i++) {
			t = Arrays.asList(tt[i]);
			List<String> temp = new ArrayList<>(t);
			int K = Integer.parseInt(temp.get(0));
			temp.remove(0);

			int j = 0;
			while(j < ans.size()) {
				if(temp.indexOf(ans.get(j)) < 0) {
					ans.remove(j);
				}else {
					j++;
				}
			}
		}

		System.out.println(ans.size());
	}
}
