package Atcoder.abc_ontime;

//台湾旅行中
import java.util.Scanner;

public class A_137 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();

		System.out.println(Math.max(Math.max(A+B, A-B), A*B));
	}
}
