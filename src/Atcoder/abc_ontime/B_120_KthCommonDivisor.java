package Atcoder.abc_ontime;

import java.util.Scanner;

public class B_120_KthCommonDivisor {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt();
		int B = sc.nextInt();
		int K = sc.nextInt();

		int kcd = gcd(A,B);
		int count = 0;

		for(int i=kcd;i>0;i--) {
			if(kcd%i == 0) {
				count++;
			}

			if(count == K) {
				System.out.println(i);
				break;
			}
		}

	}

	public static int gcd(int m,int n){
		if(n == 0){
			return m;
		}else{
			return gcd(n,m%n);
		}
	}

}
