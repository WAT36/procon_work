package p201_fullSearch;

import java.util.ArrayList;

/**
 * キューのデータ構造を表したクラス
 * （）
 * 
 * @author watarutsukagoshi
 *
 */
public class Queue {

	private ArrayList<Object> q = new ArrayList<>();

	public void print() {
		System.out.println(q.toString());
	}

	public void push(Object o) {
		q.add(o);
	}

	public void pop() {
		if (q.size() > 0) {
			q.remove(0);
		}
	}

	public static void main(String args[]) {

		Queue q = new Queue();

		q.print();
		q.push(0);
		q.push(1);
		q.print();
		q.push(2);
		q.pop();
		q.print();
		q.push("A");
		q.push('B');
		q.print();
	}
}
