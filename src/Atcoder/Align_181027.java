package Atcoder;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * 10/27のtenkaichi beginner contestで不正解問
 * C問題
 * 
 * @author T.Wakasugi
 *
 */
public class Align_181027 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		ArrayList<Integer> a = new ArrayList<>();
		ArrayList<Integer> b = new ArrayList<>();
		int n = Integer.parseInt(sc.nextLine());
		int diff = 0;
		for(int i=0;i<n;i++) {
			String s = sc.nextLine();
			if(s.equals("")) {
				break;
			}else {
				a.add(Integer.parseInt(s));
			}
			System.out.print(s + " ");
		}
		System.out.println("");
		Collections.sort(a);

		b.add(a.get(0));
		a.remove(0);
		int count = 1;

		while(count < n) {
			int tmp = 0;
			if(count % 2 == 0) {
				tmp = a.get(0);
				a.remove(0);
			}else {
				tmp = a.get(a.size()-1);
				a.remove(a.size()-1);
			}

			if(Math.abs(tmp - b.get(0)) > Math.abs(tmp - b.get(b.size()-1))) {
				diff += Math.abs(tmp - b.get(0));
				b.add(0, tmp);
			}else {
				diff += Math.abs(tmp - b.get(b.size()-1));
				b.add(tmp);
			}
			count++;
			System.out.println(count + "," + diff + "," + b);
		}

		System.out.println(diff);
	}

}
