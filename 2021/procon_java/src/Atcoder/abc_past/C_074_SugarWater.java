package Atcoder.abc_past;

import java.util.Scanner;

public class C_074_SugarWater {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int D = sc.nextInt();
		int E = sc.nextInt();
		int F = sc.nextInt();

		int max_sugar = 0;
		int max_sugarwater = 0;
		double max_percent = 0;
		for(int i=0;100*A*i <= F;i++) {
			for(int j=0;100*B*j <= F - 100*A*i;j++) {

				for(int k=0;C*k <= E*(A*i + B*j) && C*k <= F - (A*i + B*j);k++) {
					for(int l=0;D*l <= E*(A*i+B*j) - C*k && D*l <= F - 100*(A*i+B*j) - C*k;l++) {
						double water = 100*(A*i + B*j);
						double sugar = C*k + D*l;
						double percent = (100*sugar) / (water +sugar);

						if(percent >= max_percent) {
							max_sugar = (int)sugar;
							max_sugarwater = (int)(water+sugar);
							max_percent = percent;
						}
					}
				}
			}
		}

		System.out.println(max_sugarwater + " " + max_sugar);
	}

}
