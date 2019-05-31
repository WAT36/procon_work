package Atcoder.abc_ontime;

import java.util.Scanner;

//問題文
//とある世界では、今日はクリスマスです。
//
//高羽氏のパーティで、彼は多次元バーガーを作ることにしました。レベル L バーガー (L は 0 以上の整数) とは次のようなものです。
//レベル 0 バーガーとは、パティ 1 枚である。
//レベル L バーガー (L≥1) とは、バン 1 枚、レベル L−1 バーガー、パティ 1 枚、レベル L−1 バーガー、バン 1 枚、
//をこの順に下から積み重ねたものである。
//例えば、パティを P、バンを B で表すと、レベル 1 バーガーは BPPPB (を 90 度回転したもの)、
//レベル 2 バーガーは BBPPPBPBPPPBB といった見た目になります。
//
//高羽氏が作るのはレベル N バーガーです。ダックスフンドのルンルンは、このバーガーの下から X 層を食べます
//(パティまたはバン 1 枚を 1 層とします)。ルンルンはパティを何枚食べるでしょうか？
//
//制約
//1≤N≤50
//1≤X≤( レベル N バーガーの層の総数 )
//N,X は整数である。

//TODO 再帰を使うと大きな数の時にOutOfMemoryError発生
public class D_115_Christmas {

	public static String makeBurger(int level) {
		if(level <= 0) {
			return "P";
		}else {
			return "B" + makeBurger(level - 1) + "P" + makeBurger(level - 1) + "B";
		}
	}

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String[] s = sc.nextLine().split(" ");

		int N = Integer.parseInt(s[0]);
		int X = Integer.parseInt(s[1]);

		String burger = makeBurger(N);
		System.out.println(burger);
		String burger_sub = burger.substring(0, X);
		System.out.println(burger_sub);
		//ここ単純にfor回し・・
		//TODO 配列でもリストでも、指定された値がある要素はいくつあるか数えるメソッドとか無いかな
		int p = 0;
		for(int i=0;i<burger_sub.length();i++) {
			if(burger_sub.charAt(i) == 'P') {
				p++;
			}
		}

		System.out.println(p);
	}

	//この場合だと引数にintの最大値以上の数が来た時にエラーが発生
	//レベル５０などになった場合、普通にそれくらいの数まで行くので、、
	//
	//問題文通りにそのままアルゴリズムを考えるのではなく、
	//計算式、漸化式等を使って法則を見出し、それを書いて行く方式にする
	//(Atcoderで最初にやったコンテストみたいに)
}
