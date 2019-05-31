package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_118_Monster {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = Integer.parseInt(sc.nextLine());

		ArrayList<Integer> a = new ArrayList<>();

		String[] s = sc.nextLine().split(" ");
		for(int i=0;i<N;i++) {
			a.add(Integer.parseInt(s[i]));
		}
		Collections.sort(a);

		while(a.size() > 1) {
			int min = a.get(0);
			for(int j=1;j<a.size();j++) {
				a.set(j, a.get(j) % min);
			}
			List<Integer> temp = new ArrayList<>();
			temp.add(0);
			a.removeAll(temp);
			Collections.sort(a);
		}

		System.out.println(a.get(0));
	}

}
