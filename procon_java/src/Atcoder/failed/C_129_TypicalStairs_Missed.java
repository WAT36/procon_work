package Atcoder.failed;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class C_129_TypicalStairs_Missed {

	public static final long MOD = 1000000007;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		List<Integer> a = new ArrayList<>();
		a.add(sc.nextInt());
		for(int i=1;i<M;i++) {
			int temp = sc.nextInt();
			if(temp != a.get(a.size()-1)) {
				a.add(temp);
			}

			if (a.size() > 1 && (a.get(a.size()-1) - a.get(a.size()-2)) == 1) {
				System.out.println(0);
				return;
			}
		}

		long ans = 1;
		ans *= antotal(0,a.get(0)-1);
		for(int i=0;i<a.size()-1;i++) {
			ans *= antotal(a.get(i)+1,a.get(i+1)-1);
		}
		ans *= antotal(a.get(a.size()-1)+1,N);
		System.out.println(ans % MOD);
	}

	public static long antotal(int start,int end) {
		int interval = end - start;

		int one_num = interval;
		int two_num = 0;
		long sum = 0;
//		System.out.println(start+" "+end+" "+sum);
		if(one_num == 1) return 1;
		while(one_num >= 0) {
//			System.out.println("a1num:"+one_num+",2num:"+two_num+",sum:"+sum+"factone:"+fact(one_num)+"facttwo:"+fact(two_num));
			sum += fact(one_num + two_num)/(fact(one_num)*fact(two_num));
//			System.out.println("b1num:"+one_num+",2num:"+two_num+",sum:"+sum);
			one_num -= 2;
			two_num++;
		}
//		System.out.println(start+" "+end+" "+sum);
		return sum;
	}

	public static long fact(long i) {
		if(i <= 1) return 1;
		else return (i%MOD)*(fact(i-1)%MOD)%MOD;
	}
}
