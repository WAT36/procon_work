package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class C_111_myanswer {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int[] a = new int[n/2];
		int[] b = new int[n/2];

		for (int i = 0; i < n/2; i++) {
			a[i] = sc.nextInt();
			b[i] = sc.nextInt();
		}

		Map<Integer,List<Integer>> mode_a = mode(a);
		Map<Integer,List<Integer>> mode_b = mode(b);

		//aの最頻値

	}

	public static Map<Integer,List<Integer>> mode(int[] a) {
		Map<Integer, Integer> count = new HashMap<Integer, Integer>();
		for (int i = 0; i < a.length; i++) {
			if (count.containsKey(a[i])) {
				int temp = count.get(a[i]);
				count.put(a[i], temp + 1);
			} else {
				count.put(a[i], 1);
			}
		}

		List<Integer> key = new ArrayList<>(count.keySet());
		List<Integer> values = new ArrayList<>(count.values());

		Map<Integer,List<Integer>> count2 = new TreeMap<Integer,List<Integer>>();
		for(int i=0;i<key.size();i++) {
			if(count2.containsKey(values.get(i))) {
				List<Integer> temp = count2.get(values.get(i));
				temp.add(key.get(i));
				count2.put(values.get(i), temp);
			}else {
				List<Integer> temp = new ArrayList<>();
				temp.add(key.get(i));
				count2.put(values.get(i), temp);
			}
		}

		return count2;
	}

}
