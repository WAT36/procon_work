package Atcoder.abc_past;

import java.util.Arrays;
import java.util.Scanner;

public class D_127_IntegerCards {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[] A = new int[N];
		long sum=0;
		for(int i=0;i<N;i++) {
			A[i] = sc.nextInt();
			sum += A[i];
		}
		Arrays.sort(A);

		int[][] bc = new int[M][2];
		for(int i=0;i<M;i++) {
			bc[i][0] = sc.nextInt();
			bc[i][1] = sc.nextInt();
		}
		Arrays.sort(bc,(a,b)->Integer.compare(b[1], a[1]));

		int aj = 0,j = 0;
		for(int i=0;i<M;i++) {
//			System.out.println("i:"+i+" ,aj:"+aj+" "+A[aj]+" "+bc[i][1]);
			if(A[aj] > bc[i][1]) break;
			for(j=aj;j<aj+bc[i][0] && j<N;j++) {
				if(A[j] < bc[i][1]) {
//					System.out.print("j:"+j+" "+A[j] + " ");
					sum -= A[j];
					A[j] = bc[i][1];
					sum += A[j];
//					System.out.println(bc[i][1] + " " + sum);
				}else {
					break;
				}
			}
			aj = j;
			if(j >= N) aj = N-1;
		}
		System.out.println(sum);
	}

}
