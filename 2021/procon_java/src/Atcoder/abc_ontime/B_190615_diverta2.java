package Atcoder.abc_ontime;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class B_190615_diverta2 {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		long[][] ball = new long[N][2];
		for(int i=0;i<N;i++) {
			ball[i][0] = sc.nextLong();
			ball[i][1] = sc.nextLong();
		}


		Map<String,Long> pq = new HashMap<String,Long>();
		long maxvalue = 0;
		for(int i=0;i<N;i++) {
			for(int j=i+1;j<N;j++) {
				long p = ball[j][0] - ball[i][0];
				long q = ball[j][1] - ball[i][1];

				if(p < 0 && q < 0) {
					p = -1 * p;
					q = -1 * q;
				}else if(p < 0 && q > 0) {
					p = -1 * p;
					q = -1 * q;
				}else if(p == 0 && q < 0) {
					q = -1 * q;
				}else if(p < 0 && q == 0) {
					p = -1 * p;
				}

				String s = String.valueOf(p) + "_" + String.valueOf(q);
				if(pq.containsKey(s)) {
					long temp = pq.get(s);
					temp++;
//					System.out.print("UP!:");
					if(maxvalue < temp) {
						maxvalue = temp;
					}
					pq.put(s, temp);
//					System.out.println(s+","+temp+":::"+maxvalue + ":¥t:i:"+Arrays.toString(ball[i])+"::j:"+Arrays.toString(ball[j]));
				}else {
					pq.put(s, 1L);
					if(maxvalue < 1) maxvalue = 1;
//					System.out.println(s+","+1+":::"+maxvalue + ":¥t:i:"+Arrays.toString(ball[i])+"::j:"+Arrays.toString(ball[j]));
				}
			}
		}
		System.out.println(N - maxvalue);
	}
}
