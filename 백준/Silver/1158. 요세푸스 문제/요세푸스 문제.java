import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		Deque<Integer> q = new ArrayDeque<>();
		
		for(int i=1; i<=N; i++) {
			q.offer(i);
		}
		
		System.out.print("<");
		
		int cnt = 1;
		while(!q.isEmpty()) {
			if(cnt % K == 0) {
				System.out.print(q.peek());
				if(q.size() != 1) {
					System.out.print(", ");
				}
			}else {
				q.offer(q.peek());
			}
			q.poll();
			cnt++;
		}
		System.out.print(">");
	}

}
