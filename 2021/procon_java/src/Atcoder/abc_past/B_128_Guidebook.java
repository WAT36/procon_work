package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class B_128_Guidebook {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<String> s = new ArrayList<>();
		String[][] sp = new String[N][2];
		sc.nextLine();

		for(int i=0;i<N;i++) {
			String[] line = sc.nextLine().split(" ");
			sp[i][0] = line[0];
			sp[i][1] = String.format("%03d", Integer.parseInt(line[1]));
			s.add(sp[i][0] + "_" + sp[i][1]);
		}
		Arrays.sort(sp,(a,b)-> (a[0].equals(b[0])) ?  b[1].compareTo(a[1]) : a[0].compareTo(b[0]));
		for(int i=0;i<N;i++) {
			System.out.println(s.indexOf(sp[i][0] + "_" + sp[i][1]) + 1);
		}
	}
}
