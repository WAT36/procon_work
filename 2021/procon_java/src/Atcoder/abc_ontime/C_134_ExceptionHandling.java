package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_134_ExceptionHandling {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Integer> A = new ArrayList<>();

		for(int i=0;i<N;i++) {
			A.add(sc.nextInt());
		}
		int max = Collections.max(A);
		int max_i = A.indexOf(max);
		List<Integer> temp = new ArrayList<>(A);
		temp.remove(max_i);
		int second_max = Collections.max(temp);

		for(int i=0;i<N;i++) {
			if(i == max_i) {
				System.out.println(second_max);
			}else {
				System.out.println(max);
			}
		}
	}
}
