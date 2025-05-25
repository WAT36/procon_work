package Atcoder.abc_past;

import java.util.Scanner;

public class C_ABC099_StrangeBank {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		System.out.println(calc(N,0));
	}

	public static int calc(int n,int ans) {

		if(n < 6) return ans + n;

//		int a = (int)Math.pow(6,Math.floor(Math.log(n)/Math.log(6)));
//		int b = (int)Math.pow(9,Math.floor(Math.log(n)/Math.log(9)));
		int a=1,b=1;
		while(a*6<=n) a*=6;
		while(b*9<=n) b*=9;

		return Math.min(calc(n-a,ans+1),calc(n-b,ans+1));
	}

}
