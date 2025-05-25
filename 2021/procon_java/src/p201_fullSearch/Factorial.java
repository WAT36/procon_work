package p201_fullSearch;


/**
 * 数値iの階乗を計算する
 *
 * @author watarutsukagoshi
 *
 */
public class Factorial {

	/**
	 * iの階乗を計算するメソッド
	 *
	 * @param i
	 * @return
	 */
	public int calcFact(int i) {

		if(i < 0) {
			return 0;
		}else if(i > 1) {
			return i * calcFact(i - 1);
		}else {
			return 1;
		}

	}


	public static void main(String args[]) {

		Factorial f = new Factorial();

		for(int i = 5;i>0;i--){
			System.out.println(i+":	"+f.calcFact(i));
		}

	}
}
