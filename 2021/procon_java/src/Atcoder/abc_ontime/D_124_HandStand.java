package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class D_124_HandStand {


	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		sc.nextLine();
		String s = sc.nextLine();

		List<Integer> stand = new ArrayList<>();
		List<Integer> hand = new ArrayList<>();

		char flag = '0';
		int count = 0;
		for(int i=0;i<N;i++) {

			if(s.charAt(i) == flag) {
				count++;
			}else if(flag == '0'){
				stand.add(count);
				count = 1;
				flag = '1';
			}else {
				hand.add(count);
				count = 1;
				flag = '0';
			}
		}

		if(flag == '0') {
			stand.add(count);
			flag = '1';
			count = 0;
		}
		if(flag == '1') hand.add(count);

		for(int i=0;i<K;i++) {
			int index = maxhandstandindex(stand, hand);

			if(index != 0) {
				hand.set(index-1, hand.get(index-1) + stand.get(index) + hand.get(index));
				hand.remove(index);
				stand.remove(index);
			}else {
				hand.set(index, stand.get(index) + hand.get(index));
				stand.set(index, 0);
			}
		}

		System.out.println(Collections.max(hand));
	}

	public static int maxhandstandindex(List<Integer> stand,List<Integer> hand) {
		List<Integer> sum = new ArrayList<>();

		for(int i=0;i<Math.min(stand.size(), hand.size());i++) {
			sum.add(stand.get(i) + hand.get(i));
		}

		return sum.indexOf(Collections.max(sum));
	}

}
