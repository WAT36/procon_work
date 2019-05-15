package Atcoder.abc_ontime;

import java.util.Arrays;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class C_121_Energy {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		int[] A = new int[N];
		Map<Integer,Integer> map = new TreeMap<Integer, Integer>();
		for(int i=0;i<N;i++) {
			A[i] = sc.nextInt();
			int b = sc.nextInt();

			if(map.containsKey(A[i])) {
				int temp = map.get(A[i]);
				map.remove(A[i]);
				map.put(A[i], temp+b);
				A[i] = Integer.MAX_VALUE;
			}else {
				map.put(A[i], b);
			}
		}
		Arrays.sort(A);

		long yen = 0;
		for(int i=0;i<A.length;i++) {
			if(M > map.get(A[i])) {
				yen += ((long)A[i] * (long)map.get(A[i]));
				M -= map.get(A[i]);
			}else {
				yen += ((long)A[i] * (long)M);
				break;
			}
		}
		System.out.println(yen);
	}
}
