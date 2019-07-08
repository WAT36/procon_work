package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class A_AGC032_LimitedInsertion {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Integer> b = new ArrayList<>();

		for(int i=0;i<N;i++) {
			b.add(sc.nextInt());
		}

		List<Integer> ans = listsearch(b,new ArrayList<Integer>());
		if(ans.size() == 0) {
			System.out.println(-1);
		}else {
			for(int i=ans.size()-1;i>=0;i--) {
				System.out.println(ans.get(i));
			}
		}

	}

	public static List<Integer> listsearch(List<Integer> b,List<Integer> ans) {

		if(b.size() == 0) return ans;

		List<Integer> b_temp;
		List<Integer> ans_temp;

		for(int i=b.size()-1;i>=0;i--) {
			if(b.get(i) == i+1) {
				b_temp = new ArrayList<>(b);
				ans_temp = new ArrayList<>(ans);
				b.remove(i);
				ans.add(i+1);
				List<Integer> c = listsearch(b,ans);
				if(c.size() != 0) {
					return c;
				}else {
					return new ArrayList<Integer>();
				}
			}
		}
		return new ArrayList<Integer>();
	}
}
