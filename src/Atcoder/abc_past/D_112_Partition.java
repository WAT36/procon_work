package Atcoder.abc_past;

import java.util.Scanner;
import java.util.TreeSet;

public class D_112_Partition {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		TreeSet<Integer> x = new TreeSet<>();
		for (int i = 1; i*i <= M; i++) {
			if (M % i == 0) {
				x.add(i);
				x.add(M / i);
			}
		}

		System.out.println(M/x.ceiling(N));

//		x = new ArrayList<>(t);
//		Collections.sort(x);
//
//		int ans = 0;
//		for (int i = 0; i < x.size(); i++) {
//			if(M/N >= x.get(i)) {
//				ans = x.get(i);
//			}else {
//				System.out.println(ans);
//				break;
//			}
//		}
	}
}
