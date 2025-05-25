package Atcoder.abc_ontime;

import java.util.Arrays;
import java.util.Scanner;

public class C_117_Streamline {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		int N = Integer.parseInt(s.split(" ")[0]);
		int M = Integer.parseInt(s.split(" ")[1]);

		s = sc.nextLine();
		String[] xs = s.split(" ");
		int[] x = new int[M];
		for (int i = 0; i < M; i++) {
			x[i] = Integer.parseInt(xs[i]);
		}

		Arrays.sort(x);

		int[] diff = new int[M - 1];
		for (int i = 0; i < M - 1; i++) {
			diff[i] = x[i + 1] - x[i];
		}
		Arrays.sort(diff);

		int ans = 0;
		for (int i = 0; i < M - N; i++) {
			ans += diff[i];
		}

		System.out.println(ans);

	}

}
