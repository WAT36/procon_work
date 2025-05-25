package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_ARC059_betogether {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Integer> a = new ArrayList<>();
		for(int i=0;i<N;i++) {
			a.add(sc.nextInt());
		}
		int min = Collections.min(a);
		int max = Collections.max(a);

		long ans = Long.MAX_VALUE;
		for(int i=min;i<=max;i++) {
			int sum = 0;
			for(int j=0;j<N;j++) {
				sum += (a.get(j) - i)*(a.get(j) - i);
			}

			if(ans > sum) {
				ans = sum;
			}
		}
		System.out.println(ans);
	}

}
