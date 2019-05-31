package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_107_Candle {
	
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		List<Integer> x = new ArrayList<>();
		List<Integer> abs = new ArrayList<>();
		for(int i=0;i<N;i++) {
			int temp = sc.nextInt();
			x.add(temp);
			abs.add(Math.abs(temp));
		}
		
		int time = 0;
		for(int i=0;i<K;i++) {
			int min = 0;
			min = Collections.min(abs);
			time += min;
			
			int index = abs.indexOf(min);
			x.remove(index);
			abs.remove(index);
			
			for(int j=0;j<x.size();i++) {
				int temp = x.get(j);
				x.set(j, temp);
			}
		}
	}

}
