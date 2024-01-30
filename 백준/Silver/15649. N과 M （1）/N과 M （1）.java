import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main{
	
	static boolean[] check;
	static int n;
	static int m;
	static  Deque<Integer> list;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		check = new boolean[n+1];
		list = new ArrayDeque<>();
		
		backTracking();
	}
	
	public static void backTracking() {
		if (list.size() == m) {
			for(int i:list) {
				System.out.print(i+" ");
			}
			System.out.println("");
			return;
		}
		for(int i = 1; i<n+1; i++) {
			if (check[i] == false) {
				check[i] = true;
				list.add(i);
				backTracking();
				check[i] = false;
				list.removeLast();
			}
		}
	}
}