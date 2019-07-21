package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class D_134_PreparingBox {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] a = new int[N+1];

		for(int i=1;i<=N;i++) {
			a[i] = sc.nextInt();
		}

		int[] b = new int[N+1];
		List<Integer> balli = new ArrayList<>();

		int M = N;
		int balls = 0;

		for(int i=N;i>0;i--) {

			int iball = 0;
			for(int k=2;k*i <= N;k++) {
				iball += b[k*i];
			}

			if(iball % 2 == a[i]) {
				b[i] = 0;
			}else {
				b[i] = 1;
				balli.add(i);
			}
		}

		System.out.println(balli.size());
		for(int i=balli.size()-1;i>=0;i--) {
			System.out.println(balli.get(i));
		}

//		for(int i=0;i<Math.floor(Math.log(N)/Math.log(2))+1;i++) {
//
//			int start;
//			if(M%2 == 0) {
//				start = M/2;
//			}else {
//				start = (int) Math.ceil((double)M/(double)2);
//			}
//
//			for(int j=start;j<=M;j++) {
//				int iball =0;
//
//				for(int k=2;k*j<=N;k++) {
//					iball += b[k*j];
//				}
//
//				if(iball % 2 == a[j]) {
//					b[j] = 0;
//				}else {
//					b[j] = 1;
//					balli.add(j);
//					balls++;
//				}
//
//			}
//
//			if(start == 2) {
//				M = 1;
//			}else if(M%2 == 0) {
//				M = M/2;
//			}else {
//				M = (int) Math.floor((double)M/(double)2);
//			}
//
//		}
//
//		Collections.sort(balli);
//		System.out.println(balls);
//		for(int i=0;i<balli.size();i++) {
//			System.out.print(balli.get(i) + " ");
//		}
//		System.out.println();
	}
}
