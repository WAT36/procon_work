package Atcoder.abc_past;

import java.util.Scanner;

public class B_075_MineSweeper {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int H = sc.nextInt();
		int W = sc.nextInt();
		StringBuilder[] S = new StringBuilder[H];
		sc.nextLine();

		for(int i=0;i<H;i++) {
			S[i] = new StringBuilder(sc.nextLine());
		}

		for(int i=0;i<H;i++) {
			for(int j=0;j<W;j++) {
				if(S[i].charAt(j) == '.') {
					int mine = CalcMine(S,i,j);
					S[i].setCharAt(j, (char)(mine + 48));
				}
			}
		}

		for(int i=0;i<H;i++) {
			System.out.println(S[i].toString());
		}


	}

	public static int CalcMine(StringBuilder[] s,int h,int w) {

		int mine = 0;
		int H = s.length;
		int W = s[0].length();
		if(w > 0 			&& s[h].charAt(w-1) == '#') mine++;		//左
		if(w > 0 && h > 0 	&& s[h-1].charAt(w-1) == '#') mine++;	//左上
		if(h > 0 			&& s[h-1].charAt(w) == '#') mine++;		//上
		if(h > 0 && w < W-1	&& s[h-1].charAt(w+1) == '#') mine++;	//右上
		if(w < W-1 			&& s[h].charAt(w+1) == '#') mine++;		//右
		if(h < H-1 && w < W-1 && s[h+1].charAt(w+1) == '#') mine++;	//右下
		if(h < H-1 			&& s[h+1].charAt(w) == '#') mine++;		//下
		if(h < H-1 && w > 0 	&& s[h+1].charAt(w-1) == '#') mine++;	//左下

		return mine;
	}
}
