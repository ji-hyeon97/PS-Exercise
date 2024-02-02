import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		for(int test_case = 1; test_case<11; test_case++) {
			int n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			
			int []arr = new int[8];
			for (int i = 0; i<8; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			int index = 1;
			
			Deque<Integer> deque = new ArrayDeque<>();
			for(int i:arr) {
				deque.offer(i);
			}
			
			while (true){
				int a = deque.pollFirst();
				a -= index;
				if (a<=0) {
					deque.offer(0);
					break;
				}
				else {
					deque.offer(a);
					index+=1;
					if (index >= 6) {
						index = 1;
					}
				}
			}
			System.out.print("#"+test_case+" ");
			for(int i:deque) {
				System.out.print(i+" ");
			}
			System.out.println();
		}
	}
}