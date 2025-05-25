package Atcoder.abc_past;

import java.util.Scanner;

public class C_133_RemainderMinimization2019 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long L = sc.nextLong();
		long R = sc.nextLong();

		if(R-L >= 2019) {
			System.out.println(0);
		}else {
			long ans = 2019;
			for(long i=L;i<=R;i++) {
				for(long j=i+1;j<=R;j++) {
					if(i*j % 2019 < ans) {
						ans = i*j % 2019;
					}

					if(ans == 0) {
						System.out.println(0);
						return;
					}
				}
			}
			System.out.println(ans);
		}
	}

}
