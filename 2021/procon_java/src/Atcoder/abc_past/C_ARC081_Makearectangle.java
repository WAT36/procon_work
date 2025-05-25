package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class C_ARC081_Makearectangle {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] a = new long[N];
		for(int i=0;i<N;i++) {
			a[i] = sc.nextLong();
		}
		Arrays.sort(a);
		int count=0;
		long pre = a[a.length-1];
		List<Long> l = new ArrayList<>();
		for(int i=a.length-1;i>=0;i--) {
			if(a[i] == pre) {
				count++;
			}else {
				count = 1;
			}
			pre = a[i];

			if(count % 2 == 0) l.add(a[i]);
			if(l.size() >= 2) break;
		}

		if(l.size() < 2) {
			System.out.println(0);
		}else {
			System.out.println(l.get(0) * l.get(1));
		}
	}
}
