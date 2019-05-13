package mylib;

public class Math {

	//整数a,bの最大公約数
	public static int gcd(int a,int b) {
		if(b == 0) return a;
		else return gcd(b,a%b);
	}

	//整数a,bの最小公倍数
	public static int lcm(int a,int b) {
		return a*b/gcd(a,b);
	}

}
