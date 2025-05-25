package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

public class D_127_IntegerCards {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		long[] A = new long[N];
		long[] B = new long[M];
		long[] C = new long[M];
		Map<Long,Long> bc = new TreeMap<Long,Long>();

		for (int i = 0; i < N; i++) {
			A[i] = sc.nextLong();
		}

		for (int i = 0; i < M; i++) {
			long bi = sc.nextLong();
			long ci = sc.nextLong();
			if(bc.containsKey(ci)) {
				long b = bc.get(ci);
				bc.put(ci, b + bi);
			}else {
				bc.put(ci, bi);
			}
		}

		Arrays.sort(A);

		Set bc_keyset = bc.keySet();
		List<Long> bc_list = new ArrayList<>(bc_keyset);
		Collections.reverse(bc_list);

		int count = 0;
		for (long i : bc_list) {
			if(i <= A[0]) break;

			for (int j = 0; j < N; j++) {
//				System.out.println("count:"+count + " A["+j+"]:"+A[j]+" B:"+bc.get(i)+" C:"+i);
				long b = bc.get(i);
				if (count < b && A[j] < i) {
					A[j] = i;
					count++;
				}else if(count >= b || A[j] >= i) {
					break;
				}
			}
			Arrays.sort(A);
			count = 0;
//			System.out.println(Arrays.toString(A));
		}

		long ans = 0;
		for(int i=0;i<N;i++) {
			ans += A[i];
		}
		System.out.println(ans);
	}
}
