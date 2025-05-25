package p201_fullSearch;

/**
 * 数値iのフィボナッチ数を計算する
 *
 * @author watarutsukagoshi
 *
 */
public class Fibonacci {

	/**
	 * 数値iのフィボナッチ数を計算する
	 * 
	 * @param i
	 * @return
	 */
	public int calcFib(int i) {

		if(i <= 0) {
			return -1;
		}else if(i == 1 || i == 2) {
			return 1;
		}else {
			return calcFib(i-1) + calcFib(i-2);
		}
	}

	public static void main(String args[]) {

		Fibonacci f = new Fibonacci();

		for(int i=1;i<=10;i++) {
			System.out.println(i+": "+f.calcFib(i));
		}
	}
}
