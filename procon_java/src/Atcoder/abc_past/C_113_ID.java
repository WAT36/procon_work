package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class C_113_ID {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		ArrayList<ArrayList<Long>> py = new ArrayList<ArrayList<Long>>();
		Map<Integer,Long> iy = new TreeMap<>();
		Map<Long,Integer> yp = new TreeMap<>();
		for(int i=0;i<N;i++) {
			ArrayList<Long> p = new ArrayList<>();
			py.add(p);
		}

		for(int i=0;i<M;i++) {
			int P = sc.nextInt();
			long Y = sc.nextInt();
			iy.put(i, Y);
			yp.put(Y, P);
			py.get(P-1).add(Y);
			Collections.sort(py.get(P-1));
		}

		for(int i=0;i<M;i++) {
			long y = iy.get(i);
			int p = yp.get(y);
			int x = py.get(p-1).indexOf(y);
			String pref = "000000" + String.valueOf(p);
			pref = pref.substring(pref.length() - 6);
			String X = "000000" + String.valueOf(x+1);
			X = X.substring(X.length() - 6);
			System.out.println(pref + X);
		}
	}
}
