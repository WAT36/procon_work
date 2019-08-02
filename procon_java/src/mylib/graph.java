package mylib;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class graph {

	// 頂点の訪問状態、WHITE:未訪問、GLAY:訪問中、BLACK:訪問済
	public static final int WHITE = 0;
	public static final int GLAY = 1;
	public static final int BLACK = 2;

	// グラフ（隣接リスト形式、(頂点のインデックス、隣接する頂点のインデックスのリスト)）
	// 隣接する点がないときは空のリストをいれる
	public static Map<Integer, List<Integer>> graph = new HashMap<>();

	// スタックによるグラフの深さ優先探索、ここでは訪問時間の配列を返す。何を取得したいかで戻り値は変えること
	// 引数　first:最初に訪問する頂点  N:頂点の数  graph:グラフ（隣接リスト形式）
	public static int[][] depth_stack(int first,int N,Map<Integer, List<Integer>> graph) {

		// 頂点が訪問済みかを記録する配列。0:未訪問、1:訪問中、2:訪問済
		int[] color = new int[N];
		// 時間
		int time = 0;
		// 最初に訪問した時間/訪問終了の時間 の配列
		int[][] df = new int[N][2];

		// 探索用スタック
		List<Integer> stack = new ArrayList<>();
		// 始点firstをスタックに追加
		stack.add(first);
		color[first] = GLAY;
		df[first][0] = ++time;;

		while (!stack.isEmpty()) {
			// スタックの一番上の点
			int top_v = stack.get(stack.size() - 1);

			// スタックの一番上の点 に隣接する点のリスト
			List<Integer> vlist = graph.get(top_v);
			// 隣接する点のリストから最初の訪問済ではない点を取得、全て訪問済みなら -1 とする
			int i = 0;
			while (i < vlist.size() && (color[vlist.get(i)] == BLACK || color[vlist.get(i)] == GLAY))
				i++;
			int next_v = (i < vlist.size()) ? vlist.get(i) : -1;
			System.out.println(top_v + "," + next_v);
			if (next_v != -1) {
				// 隣接点がある
				if (color[next_v] == WHITE) {
					color[next_v] = GLAY;
					df[next_v][0] = ++time;
					stack.add(next_v);
				}
			} else {
				// 隣接点がない
				stack.remove(stack.size() - 1);
				color[top_v] = BLACK;
				df[top_v][1] = ++time;
			}
		}
		return df;
	}

	// テスト用
	public static void main(String[] args) {

		//初期化
		graph.clear();
		graph.put(0, Arrays.asList(new Integer[] {1,2,4}));
		graph.put(1, Arrays.asList(new Integer[] {0,2,3}));
		graph.put(2, Arrays.asList(new Integer[] {0,1,3,4,5}));
		graph.put(3, Arrays.asList(new Integer[] {1,2,6}));
		graph.put(4, Arrays.asList(new Integer[] {0,2}));
		graph.put(5, Arrays.asList(new Integer[] {2,6}));
		graph.put(6, Arrays.asList(new Integer[] {2,3,5}));

		List<Integer> temp = graph.get(0);
		for(int i=0;i<temp.size();i++) {
			System.out.println(temp.get(i));
		}

		int[][] ans = depth_stack(0,7,graph);
		for(int i=0;i<ans.length;i++) {
			System.out.println(i + ":(" + ans[i][0] + "," + ans[i][1] + ")");
		}

	}

}
