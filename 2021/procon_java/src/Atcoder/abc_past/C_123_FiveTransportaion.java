package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class C_123_FiveTransportaion {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		List<Long> trans = new ArrayList<>();

		for (int i = 0; i < 5; i++) {
			trans.add(sc.nextLong());
		}

		Long min_t = Collections.min(trans);
		Long temp = (long)Math.ceil((double)N/(double)min_t);
		System.out.println(5 + temp - 1);

	}

}
