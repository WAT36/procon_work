package Atcoder.abc_ontime;

import java.util.Arrays;
import java.util.Scanner;

public class B_117_Polygon {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		int N = Integer.parseInt(s);

		s = sc.nextLine();
		String[] ns = s.split(" ");

		int n[] = new int[ns.length];
		for(int i=0;i<ns.length;i++) {
			n[i] = Integer.parseInt(ns[i]);
		}

		Arrays.sort(n);

		int sum=0;
		for(int i=0;i<n.length-1;i++) {
			sum += n[i];
		}

		if(sum > n[n.length - 1]) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}
}
