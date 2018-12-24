package p202_greedy;

import java.util.Scanner;

//この問題変では・・・？
public class Coin {



	//模範解答
	public static void greedyans(int[] coin,int yen) {
		int[] kingaku = { 500, 100, 50, 10, 5, 1 };
		int ans = 0;

		for(int i=0;i < 6;i++) {
			int t = Math.min(yen/kingaku[i] + 1, coin[i]);
			yen -= t * kingaku[i];
			ans += t;
		}

		if (yen > 0) {
			System.out.println("払えない( "+ yen +" 円不足)");
		} else {
			int maisusum=0;
			for (int j = 0; j < 6; j++) {
				System.out.println(kingaku[j]+"円 "+coin[j] + " ");
				maisusum += coin[j];
			}
			System.out.println("払える (" +maisusum+ "枚)");
		}
		System.out.println();

	}

	public static void greedy(int[] coin, int yen) {

		int[] kingaku = { 500, 100, 50, 10, 5, 1 };
		int[] maisu = new int[6];
		int i = 0;

		while (true) {

			if (i >= 6 || yen <= 0) {
				break;
			} else if (coin[i] <= 0) {
				i++;
			} else {
				maisu[i]++;
				coin[i]--;
				yen -= kingaku[i];
				//System.out.println(kingaku[i] + "円");
			}

		}

		if (yen > 0) {
			System.out.println("払えない( "+ yen +" 円不足)");
		} else {
			int maisusum=0;
			for (int j = 0; j < maisu.length; j++) {
				System.out.println(kingaku[j]+"円 "+maisu[j] + " ");
				maisusum += maisu[j];
			}
			System.out.println("払える (" +maisusum+ "枚)");
		}
		System.out.println();
	}

	public static void main(String args[]) {

		int[] coin = new int[6];
		int yen = 0;

		System.out.print("Coins(500 100 50 10 5 1):");
		Scanner sc = new Scanner(System.in);
		String coins = sc.nextLine();
		String[] coinnum;

		if (coins.split(" ").length != 6) {
			System.out.println("Usage: 500 100 50 10 5 1");
			System.exit(-1);
		} else {
			coinnum = coins.split(" ");
			try {
				for (int i = 0; i < 6; i++) {
					coin[i] = Integer.parseInt(coinnum[i]);
				}

				System.out.print("yen:");
				yen = sc.nextInt();

			} catch (NumberFormatException e) {
				System.err.println("数字変換エラー");
				System.exit(-1);
			}
		}

		greedy(coin, yen);

		greedyans(coin,yen);
	}
}
