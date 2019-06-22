package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class C_082_GoodSequence {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		Map<Integer,Integer> index = new TreeMap<>();
		for(int i=0;i<N;i++) {
			int a = sc.nextInt();
			if(index.containsKey(a)) {
				int v = index.get(a);
				v++;
				index.put(a, v);
			}else {
				index.put(a, 1);
			}
		}

		List<Integer> key = new ArrayList<>(index.keySet());
		long ans = 0;
		for(int i=0;i<key.size();i++) {
			int k = key.get(i);
			int a = index.get(k);
			if(a < k) {
				ans += a;
			}else if(a > k){
				ans += a-k;
			}
		}
		System.out.println(ans);
	}
}
