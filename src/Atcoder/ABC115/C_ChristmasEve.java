package Atcoder.ABC115;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

//問題文
//とある世界では、今日はクリスマスイブです。
//
//高羽氏の庭には N 本の木が植えられています。
//i 本目の木 (1≤i≤N) の高さは hi メートルです。彼は、これらの木のうち
//K 本を選んで電飾を施すことにしました。より美しい光景をつくるために、できるだけ近い高さの木を飾り付けたいです。
//
//より具体的には、飾り付ける木のうち最も高いものの高さを
//hmax メートル、最も低いものの高さを hmin メートルとすると、hmax−hmin が小さいほど好ましいです。
//hmax−hmin は最小でいくつにすることができるでしょうか？
//
//制約
//2≤K<N≤10^5
//1≤hi≤10^9
//hi は整数である。


public class C_ChristmasEve {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String[] nk = sc.nextLine().split(" ");

		int N = Integer.parseInt(nk[0]);
		int K = Integer.parseInt(nk[1]);

		List<Integer> h = new ArrayList<>();
		for(int i=0;i<N;i++) {
			h.add(sc.nextInt());
		}

		//線形探索・・通っちゃった。時間オーバーで通るわけないと思ったのに
		Collections.sort(h);
		int min = Integer.MAX_VALUE;

		for(int i=0;i<=(N-K);i++) {
			if(min > (h.get(i+K-1) - h.get(i))) {
				min = (h.get(i+K-1) - h.get(i));
			}
		}

		System.out.println(min);
	}
}
