package Atcoder.failed;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class C_ARC084_SnukeFestival {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Set<Integer> A = new TreeSet<>();
		Set<Integer> B = new TreeSet<>();
		Set<Integer> C = new TreeSet<>();

		for(int i=0;i<N;i++) {
			A.add(sc.nextInt());
		}
		List<Integer> a = new ArrayList<>(A);

		for(int i=0;i<N;i++) {
			B.add(sc.nextInt());
		}
		List<Integer> b = new ArrayList<>(B);

		for(int i=0;i<N;i++) {
			C.add(sc.nextInt());
		}
		List<Integer> c = new ArrayList<>(C);

		int ans = 0;
//		for(int i=0;i<a.size();i++) {
//			if(a.get(i) >= b.get(b.size()-1)) continue;
//			for(int j=0;j<b.size();j++) {
//				if(a.get(i) >= b.get(j)) continue;
//				for(int k=0;k<c.size();k++) {
//					if(b.get(j) >= c.get(k)) continue;
//					String s = String.valueOf(a.get(i)) +" "+ String.valueOf(b.get(j)) +" "+ String.valueOf(c.get(k));
//					System.out.println(s);
//					ans.add(s);
//				}
//			}
//		}
//		System.out.println(a.toString());
//		System.out.println(c.toString());
		for(int i=0;i<b.size();i++) {
			int ai = binaryA(a,b.get(i));
			int ci = binaryB(c,b.get(i));
			ci = c.size() - ci;
//			System.out.println(ai+" "+ci+" "+b.get(i));
			ans += ai*ci;
		}

		System.out.println(ans);
	}

	public static int binaryA(List<Integer> a,int x) {
		int left = 0;
		int right = a.size();
		while(left < right) {
			int mid = (left + right)/2;
			if(x <= a.get(mid)) 	right = mid;
			else left = mid + 1;
		}
		return left;
	}

	public static int binaryB(List<Integer> a,int x) {
		int left = 0;
		int right = a.size();
		while(left < right) {
			int mid = (left + right)/2;
			if(x >= a.get(mid)) 	left = mid + 1;
			else right = mid;
		}
		return left;
	}
}