package ARC20190330_EXAWizard;

import java.util.Scanner;

public class B_RedBlue {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		sc.nextLine();
		String line = sc.nextLine();

		int r = 0;
		int b = 0;
		for(int i=0;i<N;i++) {
			if(line.charAt(i) == 'R') {
				r++;
			}else if(line.charAt(i) == 'B'){
				b++;
			}
		}

		if(r>b) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}

}
