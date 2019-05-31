package Atcoder.arc_ontime.arc_190508_diverta;

import java.util.Scanner;

public class C_ABsubstring {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		sc.nextLine();

		String[] s = new String[N];

		int ab = 0;
		int b_a = 0;
		int a_end = 0;
		int b_start = 0;
		for(int i=0;i<N;i++) {
			s[i] = sc.nextLine();

			int fromIndex = 0;
			while((fromIndex = s[i].indexOf("AB", fromIndex)) != -1) {
				fromIndex++;
				ab++;
			}

			if(s[i].endsWith("A") && s[i].startsWith("B")) {
				b_a++;
				continue;
			}

			if(s[i].endsWith("A")) a_end++;
			if(s[i].startsWith("B")) b_start++;
		}

		if(b_a > 0) b_a--;
		b_a += Math.min(a_end, b_start);
		if(a_end != b_start) b_a++;

		System.out.println(ab + b_a);
	}

}
