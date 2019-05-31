package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_113_ID {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String[] s = sc.nextLine().split(" ");

		int N = Integer.parseInt(s[0]);
		int M = Integer.parseInt(s[1]);

		List<ArrayList<Integer>> num = new ArrayList<ArrayList<Integer>>();
		List<String> numlist = new ArrayList<String>();

		for(int i=0;i<N;i++) {
			ArrayList<Integer> l = new ArrayList<Integer>();
			num.add(l);
		}

		for(int i=0;i<M;i++) {
			s = sc.nextLine().split(" ");
			int p = Integer.parseInt(s[0]);
			int y = Integer.parseInt(s[1]);
			num.get(p-1).add(y);
		}

		for(int i=0;i<N;i++) {
			for(int j=0;j<num.get(i).size();j++) {
				StringBuffer n = new StringBuffer(String.format("%06d", i+1) + String.format("%06d", j+1));
				numlist.add(n.reverse().toString());
			}
		}
		Collections.sort(numlist);
		for(int i=numlist.size()-1;i>=0;i--) {
			System.out.println(new StringBuffer(numlist.get(i)).reverse().toString());
		}
	}
}
