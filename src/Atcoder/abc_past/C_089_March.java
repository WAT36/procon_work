package Atcoder.abc_past;

import java.util.Scanner;

public class C_089_March {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		sc.nextLine();

		String[] S = new String[N];
		long[] march = new int[5];
		for(int i=0;i<N;i++) {
			S[i] = sc.nextLine();

			switch(S[i].charAt(0)) {
				case 'M':
					march[0]++;
					break;
				case 'A':
					march[1]++;
					break;
				case 'R':
					march[2]++;
					break;
				case 'C':
					march[3]++;
					break;
				case 'H':
					march[4]++;
					break;
				default:
					break;
			}
		}

		long ans=0;
		for(int i=0;i<3;i++) {
			if(march[i] == 0) continue;
			for(int j=i+1;j<4;j++) {
				if(march[j] == 0) continue;
				for(int k=j+1;k<5;k++) {
					if(march[k] == 0) continue;
					ans += march[i]*march[j]*march[k];
				}
			}
		}
		System.out.println(ans);
	}
}
