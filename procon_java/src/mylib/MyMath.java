package mylib;

public class MyMath {

	//整数a,bの最大公約数
	public static int gcd(int a,int b) {
		if(b == 0) return a;
		else return gcd(b,a%b);
	}

	//整数a,bの最小公倍数
	public static int lcm(int a,int b) {
		return a*b/gcd(a,b);
	}

	//底が２の対数を算出
	public static double log2(double a) {
		return Math.log(a)/Math.log(2);
	}

	//整数aが２のべき乗であるかを判定する
	public static boolean ispow2(int a) {
		int x = a & (a - 1);
		if (x == 0) {
			return true;
		} else {
			return false;
		}
	}

	//m以上n以下でのaの倍数の個数
	//(ABC131-C)しかしこれよりもn/a - m/a での方が早い
	public static long divisornum(double m,double n,double a) {
		long mindiv = (long) Math.ceil(m/a);
		long maxdiv = (long) Math.floor(n/a);
		return (maxdiv - mindiv) + 1;
	}


}
