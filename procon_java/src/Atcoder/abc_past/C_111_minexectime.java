package Atcoder.abc_past;

import java.util.Scanner;

public class C_111_minexectime {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int[] v = new int[n];

		int[] a = new int[100000];
		int[] b = new int[100000];

		for(int i=0;i<n;i++) {
			v[i] = sc.nextInt();
		}

		for(int i=0;i<n;i+=2) {
			a[v[i]]++;
			b[v[i+1]]++;
		}

		int maxa=0,maxb=0;
		for(int i=0;i<100000;i++) {
			if(a[i] > a[maxa]) maxa = i;
			if(b[i] > b[maxb]) maxb = i;
		}

		if(maxa == maxb) {
			int t1=0,t2=0;
			for(int i=0;i<100000;i++) {
				if(a[i] > a[t1] && i != maxb) t1 = i;
				if(b[i] > b[t2] && i != maxa) t2 = i;
			}

			System.out.println(Math.min((n - a[maxa] - b[t2]),(n - b[maxb] - b[t2])));
		}else {
			System.out.println(n - a[maxa] - b[maxb]);
		}
	}
}
