package p203_dynamic;

import java.util.Scanner;

/**
 * @author watarutsukagoshi
 *
 * ２つの文字列s1s2...snとt1t2...tmが与えられます。
 * これら２つの共通部分文字列の長さの最大値を求めなさい。
 * 文字列s1s2...snの部分文字列とは、si1si2...simと表すことのできる文字列のことを言う。
 *
 */
public class LongestStringCoincide {


	static int n,m;
	static String s,t;

	static int i=0;

	public void init() {

		Scanner sc = new Scanner(System.in);

		System.out.print("n : ");
		n = Integer.parseInt(sc.nextLine());

		System.out.print("m : ");
		m = Integer.parseInt(sc.nextLine());

		System.out.print("s : ");
		s = sc.nextLine();

		System.out.print("t : ");
		t = sc.nextLine();
	}

	/**
	 * @param si
	 * @param ti
	 * @return
	 *
	 * sのsi文字めをtのti文字めから探していく
	 */
	public String gen(int si,int ti,String st) {

		String res;

		if(ti > t.length()) {
			gen(si+1,i,st);
		}

		if(s.charAt(si) == t.charAt(ti)) {
			res = st.concat(s.substring(si, si));
			i=ti+1;
			gen(si+1,ti+1,res);
		}else {
			gen(si,ti+1,st);
		}

		return st;
	}

	public static void main(String args[]) {

		LongestStringCoincide lsc = new LongestStringCoincide();
		lsc.init();

		System.out.println();
	}


}
