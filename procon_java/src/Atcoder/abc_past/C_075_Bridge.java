package Atcoder.abc_past;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class C_075_Bridge {

	// 頂点の訪問状態、WHITE:未訪問、GLAY:訪問中、BLACK:訪問済
	public static final int WHITE = 0;
	public static final int GLAY = 1;
	public static final int BLACK = 2;

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[][] ab = new int[M][2];

		Map<Integer, List<Integer>> graph = new HashMap<>();

		for(int i=0;i<M;i++) {
			ab[i][0] = sc.nextInt();
			ab[i][1] = sc.nextInt();

			if(graph.containsKey(ab[i][0])) {
				List<Integer> l = graph.get(ab[i][0]);
				l.add(ab[i][1]);
				graph.put(ab[i][0], l);
			}else {
				List<Integer> l = new ArrayList<>();
				l.add(ab[i][1]);
				graph.put(ab[i][0], l);
			}

			if(graph.containsKey(ab[i][1])) {
				List<Integer> l = graph.get(ab[i][1]);
				l.add(ab[i][0]);
				graph.put(ab[i][1], l);
			}else {
				List<Integer> l = new ArrayList<>();
				l.add(ab[i][0]);
				graph.put(ab[i][1], l);
			}
		}
		int ans=0;
		for(int i=0;i<M;i++) {
			int a = ab[i][0];
			int b = ab[i][1];

			List<Integer> l = graph.get(a);
			l.remove(Integer.valueOf(b));
			graph.put(a, l);

			l = graph.get(b);
			l.remove(Integer.valueOf(a));
			graph.put(b, l);

			l = depth_stack(ab[0][0],N+1,graph);
			if(l.size() != N) {
				ans++;
			}

			l = graph.get(a);
			l.add(b);
			graph.put(a, l);

			l = graph.get(b);
			l.add(a);
			graph.put(b, l);

		}
		System.out.println(ans);
	}

	public static List<Integer> depth_stack(int first,int N,Map<Integer, List<Integer>> graph) {

		//訪問済みの頂点のリスト
		List<Integer> reached = new ArrayList<>();

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
		reached.add(first);

		while (!stack.isEmpty()) {
			// スタックの一番上の点
			int top_v = stack.get(stack.size() - 1);
			if(!reached.contains(top_v)) reached.add(top_v);

			// スタックの一番上の点 に隣接する点のリスト
			List<Integer> vlist = graph.get(top_v);
			// 隣接する点のリストから最初の訪問済ではない点を取得、全て訪問済みなら -1 とする
			int i = 0;
			while (i < vlist.size() && (color[vlist.get(i)] == BLACK || color[vlist.get(i)] == GLAY))
				i++;
			int next_v = (i < vlist.size()) ? vlist.get(i) : -1;
//			System.out.println(top_v + "," + next_v);
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
		return reached;
	}

}
