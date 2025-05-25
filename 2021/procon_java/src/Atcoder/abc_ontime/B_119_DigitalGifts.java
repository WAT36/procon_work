package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_119_DigitalGifts {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = Integer.parseInt(sc.nextLine());

		int jpy = 0;
		double btc = 0.0;

		for(int i=0;i<N;i++) {
			String[] s = sc.nextLine().split(" ");
			double x = Double.parseDouble(s[0]);
			String u = s[1];

			if(u.equals("JPY")) {
				jpy += x;
			}else {
				btc += x;
			}
		}
		System.out.println(jpy + (btc * 380000));
	}
}
