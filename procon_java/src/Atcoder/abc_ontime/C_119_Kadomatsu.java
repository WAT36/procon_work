package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_119_Kadomatsu {
	
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		String[] s = sc.nextLine().split(" ");
		
		int N = Integer.parseInt(s[0]);
		List<Integer> abc = new ArrayList<>();
		abc.add(Integer.parseInt(s[1]));
		abc.add(Integer.parseInt(s[2]));
		abc.add(Integer.parseInt(s[3]));
		
		List<Integer> l = new ArrayList<>();;
		for(int i=0;i<N;i++) {
			l.add(Integer.parseInt(sc.nextLine()));
		}
		Collections.sort(l);
		
		int mp = 0;
		
		List<ArrayList<Integer>> diff = new ArrayList<ArrayList<Integer>>();
		
		
		
	}
	
	public static void calcmp(List<Integer> l,List<Integer> abc,List<List<Integer>> d) {
		
	}

}
