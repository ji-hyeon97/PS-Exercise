import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
	
	static Deque<Character> queue;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		for (int test_case = 1; test_case<11; test_case++) {
			int n = Integer.parseInt(br.readLine());
			char[] data = br.readLine().toCharArray();
			queue = new ArrayDeque<>();
			
			for (int i = 0; i<n; i++) {
				if (data[i] == '(') {
					queue.offer(data[i]);
				}
				if (data[i] == '[') {
					queue.offer(data[i]);
				}
				if (data[i] == '{') {
					queue.offer(data[i]);
				}
				if (data[i] == '<') {
					queue.offer(data[i]);
				}
				if (data[i] == '}') {
					if (queue.size() == 0) {
						queue.offer(data[i]);
					}
					else {
						if (queue.peekLast() == '{') {
							queue.pollLast();
						}
						else {
							queue.offer(data[i]);
						}
					}
				}
				if (data[i] == '>') {
					if (queue.size() == 0) {
						queue.offer(data[i]);
					}
					else {
						if (queue.peekLast() == '<') {
							queue.pollLast();
						}
						else {
							queue.offer(data[i]);
						}
					}
				}
				if (data[i] == ']') {
					if (queue.size() == 0) {
						queue.offer(data[i]);
					}
					else {
						if (queue.peekLast() == '[') {
							queue.pollLast();
						}
						else {
							queue.offer(data[i]);
						}
					}
				}
				if (data[i] == ')') {
					if (queue.size() == 0) {
						queue.offer(data[i]);
					}
					else {
						if (queue.peekLast() == '(') {
							queue.pollLast();
						}
						else {
							queue.offer(data[i]);
						}
					}
				}
				
			}
			if (queue.size() == 0) {
				System.out.println("#"+test_case+" "+1);
			}
			else {
				System.out.println("#"+test_case+" "+0);
			}
		}
	}
}