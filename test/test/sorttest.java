package test;

import static org.junit.Assert.*;

import java.util.Random;

import org.junit.Test;

import p202_greedy.PartScheduling;

public class sorttest {

	public static final int COUNT = 1000;
	public static final int RANGE = 1000;

	@Test
	public void quicksorttest() {

		PartScheduling ps = new PartScheduling();
		int a[] = new int[5];

		Random r = new Random();

		for(int i=0;i<COUNT;i++) {

			for(int j=0;j<a.length;j++) {
				a[j] = r.nextInt(RANGE);
				System.out.print(a[j] + " ");
			}
			System.out.print("|");

			int[] b = ps.quicksort(a, 0, a.length-1);

			for(int j=0;j<b.length;j++) {
				System.out.print(b[j] + " ");
			}
			System.out.println();

			for(int j=0;j<b.length - 1;j++) {
				if(b[j] > b[j+1]) {
					System.err.println("エラー");
					fail();
				}
			}
		}

		assertEquals(0,0);
	}

}
