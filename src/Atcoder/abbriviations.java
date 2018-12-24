package Atcoder;

import java.util.Scanner;

public class abbriviations {

	int n, m;
	String s, t;

	public static long gcd(long n2, long m2) {
		return m2 > 0 ? gcd(m2, n2 % m2) : n2;
	}

	public static long min(long a,long b) {
		if(a < b) {
			return a;
		}else {
			return b;
		}
	}

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		String nm = sc.nextLine();
		String[] len = nm.split(" ");

		long n = Integer.parseInt(len[0]);
		long m = Integer.parseInt(len[1]);

		String s = sc.nextLine();
		String t = sc.nextLine();

		for (int i = 0; i < min(m,n); i++) {
			if ((((m * i) % n == 0) && ((m * i) / n < m) && (s.charAt(i) != t.charAt((int) ((m * i) / n)))) ||
				(((n * i) % m == 0) && ((n * i) / m < n) &&(t.charAt(i) != s.charAt((int) ((n * i) / m))))) {
				System.out.println("-1");
				return;
			}
		}

		System.out.println(n*m/gcd(n,m));
		return;
	}

}