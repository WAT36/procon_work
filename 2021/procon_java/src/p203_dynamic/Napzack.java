package p203_dynamic;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @author watarutsukagoshi
 *
 *重さと価値がそれぞれwi,viであるようなnこの品物があります。これらの品物から、
 *重さの総和がWを超えないように選んだ時の、価値の総和の最大値を求めなさい。
 *
 *例
 *n = 4
 *(w,v) = {(2,3),(1,2),(3,4),(2,2)}
 *W = 5
 *
 *出力
 *7(0,1,3)
 */
public class Napzack {

	static int n=0, w=0;
	static List<Integer> wv = new ArrayList<>();

	static int[][] table;

	/**
	 * i番目以降の品物から重さの総和がw以下となるように選ぶ
	 *
	 * @return
	 */
	public static int res(int i,int w) {
		int res;

		if(table[i][w] > 0) {
			return table[i][w];
		}

		if(i == n) {
			res = 0;
		}else if(w < wv.get(2*i)) {
			res = res(i+1,w);
		}else {
			res = Math.max(res(i+1,w),res(i+1,w-wv.get(2*i)) + wv.get((2*i)+1));
		}

		return table[i][w] = res;
	}

	public static void main(String args[]) {

		try {

			Scanner sc = new Scanner(System.in);
			System.out.print("n : ");
			n = Integer.parseInt(sc.nextLine());

			String line;

			for(int i=0;i<n;i++){
				System.out.print("w"+i+" v"+i+":");
				line = sc.nextLine();

				if(line.split(" ")[0].equals("q") || line.split(" ")[1].equals("q")) {
					break;
				}

				wv.add(Integer.parseInt(line.split(" ")[0]));
				wv.add(Integer.parseInt(line.split(" ")[1]));
			}

			System.out.print("w : ");
			w = Integer.parseInt(sc.nextLine());

		} catch (NumberFormatException e) {
			System.err.println(e);
			System.exit(-1);
		}

		table = new int[n+1][w+1];

		System.out.println(res(0,w));

	}

}
