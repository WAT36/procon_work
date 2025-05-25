package Atcoder.abc_ontime;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class A_129_Airplane {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		List<Integer> flight = new ArrayList<>();
		for(int i=0;i<3;i++) {
			flight.add(sc.nextInt());
		}
		Collections.sort(flight);
		System.out.println(flight.get(0) + flight.get(1));
	}
}
