package Atcoder.abc_ontime;

import java.util.Scanner;

//
//問題文
//とある世界では、今日は
//12 月 D 日です。D=25 なら Christmas, D=24 なら Christmas Eve, D=23 なら Christmas Eve Eve,
//D=22 なら Christmas Eve Eve Eve と出力するプログラムを作ってください。制約 22≤D≤25 D は整数である。
//


public class A_115_ChristmasEveEveEve {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int D = sc.nextInt();

		if(D == 25) {
			System.out.println("Christmas");
		}else if(D == 24) {
			System.out.println("Christmas Eve");
		}else if(D == 23) {
			System.out.println("Christmas Eve Eve");
		}else if(D == 22) {
			System.out.println("Christmas Eve Eve Eve");
		}

	}
}
