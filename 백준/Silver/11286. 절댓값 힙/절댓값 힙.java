import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

	static int N;	
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Node> pq = new PriorityQueue<>(); 
		
		for(int i=0; i<N; i++) {
			int x = Integer.parseInt(br.readLine());
			
			if(x == 0) {
				if(pq.isEmpty()) System.out.println("0");
				else {
					Node node = pq.poll();
					System.out.println(node.val);
				}
			}
			else {
				pq.offer(new Node(Math.abs(x), x));
			}
		}
	}
	
	static class Node implements Comparable<Node>{
		int abs;
		int val;
		
		Node(int abs, int val){
			this.abs = abs;
			this.val = val;
		}

		@Override
		public int compareTo(Node o) {
			if(this.abs == o.abs)
					return this.val - o.val;
			else
				return this.abs - o.abs;
		}
	}
}
