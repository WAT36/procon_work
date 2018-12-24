package Atcoder.ABC115;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//とある世界では、今日はクリスマスイブの前日です。
//
//高羽氏は、デパートで N 個の品物を買おうとしています。i 個目の品物 (1≤i≤N) の定価は pi 円です。
//彼は割引券を持っており、N 個のうち最も定価が高い品物 1 個を定価の半額で買うことができます。
//残りの N−1 個の品物に対しては定価を支払います。支払金額は合計でいくらになるでしょうか？
//
//制約
//2≤N≤10 100≤pi≤10000pi は偶数である。
//
//入力
//入力は以下の形式で標準入力から与えられる。
//
//N
//p1
//p2
//:
//pN

public class B_ChristmasEveEve {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		ArrayList<Integer> p = new ArrayList<>();

		for(int i=0;i<N;i++) {
			p.add(sc.nextInt());
		}

		//pの最大値
		int pmax = Collections.max(p);
		//pの中でのpmaxのインデックス
		int pind = p.indexOf(pmax);
		//pの中のpmaxを半額にする
		p.set(pind, pmax/2);

		int sum=0;
		for(int i=0;i<N;i++) {
			sum += p.get(i);
		}

		System.out.println(sum);
	}

}
