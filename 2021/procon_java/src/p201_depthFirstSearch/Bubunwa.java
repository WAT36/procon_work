package p201_depthFirstSearch;

public class Bubunwa {

	int n;
	int[] a;
	int k;

	public Bubunwa(int n, int[] a, int k) {
		this.n = n;
		this.a = a;
		this.k = k;
	}


	public boolean dfs(int i, int sum) {

		if (i > n) {
			return false;
		} else if (i == n) {
			if (sum == k) {
				System.out.println();
				System.out.print("Yes(" + k + "):");
				return true;
			}
			return false;
		}

		if (dfs(i + 1, sum + a[i])) {
			System.out.print(a[i] + " ");
			return true;
		}

		if (dfs(i + 1, sum)) {
			System.out.print(" ");
			return true;
		}

		return false;

	}

	public static void main(String args[]) {

		int[] a = {1,2,3,4,7};
		Bubunwa d = new Bubunwa(a.length, a, 13);

		if (d.dfs(0, 0)) {

		}else {
			System.out.println("No.");
		}
	}

}
