package p201_fullSearch;

import java.util.ArrayList;

/**
 * スタックのデータ構造を表すクラス
 * （ArrayListだけど・・・）
 * 
 * @author watarutsukagoshi
 *
 */
public class Stack {

	private ArrayList<Object> s = new ArrayList<>();

	public void print() {
		System.out.println(s.toString());
	}

	public void push(int i) {
		s.add(i);
	}

	public void pop() {
		if (s.size() > 0) {
			s.remove(s.size() - 1);
		}
	}

	public static void main(String args[]) {

		Stack s = new Stack();

		s.print();
		s.push(3);
		s.print();
		s.push(5);
		s.push(8);
		s.push(3);
		s.print();
		s.pop();
		s.print();
		s.pop();
		s.print();

	}
}
