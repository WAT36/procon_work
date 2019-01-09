package Atcoder.abc114;

import java.util.Scanner;

//問題文
//数字 1, 2, ..., 9 からなる文字列 S があります。 ダックスフンドのルンルンは、
//S から連続する 3 個の数字を取り出し、 1 つの整数 X としてご主人様の元に持っていきます。（数字の順番を変えることはできません。）
//ご主人様が大好きな数は 753 で、これに近い数ほど好きです。 X と 753 の差（の絶対値）は最小でいくつになるでしょうか？
//
//制約
//S は長さ 4 以上 10 以下の文字列である。S の各文字は 1, 2, ..., 9 のいずれかである。

public class B_754 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();
		int min = Integer.MAX_VALUE;

		for(int i=0;i<=(S.length()-3);i++) {
			if(min > Math.abs(Integer.parseInt(S.substring(i, i+3))-753)) {
				min = Math.abs(Integer.parseInt(S.substring(i, i+3))-753);
			}
		}

		System.out.println(min);
	}
}
