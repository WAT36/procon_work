package p202_greedy;

import java.util.Scanner;

public class PartScheduling {

	public int[] quicksort(int[] a, int i, int j) {

		int pivot = 0;

		if ((j - i) < 1) {
			for (int k = 0; k < a.length; k++) {
				System.out.print(a[k] + " ");
			}
			System.out.println("a");
			return a;
		} else {
			pivot = a[i];

			int left = i, right = j;

			while (left < right) {
//				System.out.print("pivot=" + pivot + " " + left + " " + right + ":::");
				// 配列の初めからpivot以上の要素を探す
				while (a[left] < pivot && left < j)
					left++;
//				System.out.print(left + " " + right + ":::");
				// 配列の後ろからpivot未満の要素を探す
				while (a[right] >= pivot && i < right)
					right--;
//				System.out.println(left + "(" + a[left] + ")" + right + "(" + a[right] + ")" + i + " " + j);

//				for (int k = 0; k < a.length; k++) {
//					System.out.print(a[k] + " ");
//				}

				if (left > right) {
					a = quicksort(a, i, right);
					a = quicksort(a, left, j);
					break;
				} else if (left == right) {
					a = quicksort(a, i + 1, j);
					break;
				} else {
					int swap = a[right];
					a[right] = a[left];
					a[left] = swap;
				}

			}
		}
		for (int k = 0; k < a.length; k++) {
			System.out.print(a[k] + " ");
		}
		System.out.println("b");
		return a;
	}

	public void greedy(int n, int[] s, int[] t) {
		int[] sorted_t = quicksort(t, 0, t.length - 1);

		for (int i = 0; i < sorted_t.length; i++) {
			System.out.print(sorted_t[i] + " ");
		}

	}

	public static void main(String args[]) {

		PartScheduling ps = new PartScheduling();

		Scanner sc = new Scanner(System.in);
		int n;
		int[] s;
		int[] t;
		String[] row;

		try {
			System.out.print("n:");
			n = Integer.parseInt(sc.nextLine());

			System.out.print("s:");

			row = sc.nextLine().split(" ");
			s = new int[row.length];
			for (int i = 0; i < row.length; i++) {
				s[i] = Integer.parseInt(row[i]);
			}

			System.out.print("t:");

			row = sc.nextLine().split(" ");
			t = new int[row.length];
			for (int i = 0; i < row.length; i++) {
				t[i] = Integer.parseInt(row[i]);
			}

			if (s.length != t.length) {
				System.err.println("エラー：始点終点の長さ不一致");
				System.exit(-1);
			}

			ps.greedy(n, s, t);

		} catch (NumberFormatException e) {
			System.err.println("エラー：数値変換できません");
			System.out.println(e);
			System.exit(-1);
		}

	}
}
