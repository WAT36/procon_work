package Atcoder.abc_ontime;

import java.util.Scanner;

//問題文
//七五三とは、
//7 歳、5 歳そして 3 歳の子どもの成長を祝うとある国の行事です。
//いま、高橋くんは X 歳です。今回の七五三で、高橋くんの成長は祝われるでしょうか？
//
//制約
//1≤X≤9
//X は整数である。

public class A_114_753 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int X = Integer.parseInt(sc.nextLine());

		String s = (X == 3 || X == 5 || X == 7) ? "YES" : "NO";
		System.out.println(s);
	}
}
