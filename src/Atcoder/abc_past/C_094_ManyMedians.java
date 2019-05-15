package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_094_ManyMedians {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		List<Integer> X = new ArrayList<>();
		for(int i=0;i<N;i++) {
			X.add(sc.nextInt());
		}

		List<Integer> t = new ArrayList<>(X);
		Collections.sort(t);
		int median_high = t.get(N/2);
		int median_low  = t.get(N/2 - 1);

		for(int i=0;i<N;i++) {
			int x = X.get(i);
			if(median_high == median_low) {
				System.out.println(median_high);
			}else if(x < median_high) {
				System.out.println(median_high);
			}else {
				System.out.println(median_low);
			}
		}
	}
}
