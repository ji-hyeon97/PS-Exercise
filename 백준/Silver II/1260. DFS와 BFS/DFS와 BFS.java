import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	static int N, M, V;
	static String str;
	static boolean[] visited;
	static Queue<Integer> q = new ArrayDeque<>();
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	static List<List<Integer>> list = new ArrayList<>();
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
	
		for(int i=0; i<N+1; i++) {
			list.add(new ArrayList<Integer>());
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			list.get(s).add(e);
			list.get(e).add(s);
		}
		
		for(int i=0; i<N+1; i++) {
			Collections.sort(list.get(i));
		}
		
		visited = new boolean[N+1];
		str = "";
		dfs(V);
		System.out.println(str);
		
		visited = new boolean[N+1];
		str = "";
		bfs(V);
		System.out.println(str);
	}
	
	static void dfs(int cur) {
		visited[cur] = true;
		str += cur + " ";
		
		for(int node : list.get(cur)) {
			if(!visited[node]) {
				dfs(node);
			}
		}
	}
	
	static void bfs(int start) {
		q.offer(start);
		visited[start] = true;
		
		while(!q.isEmpty()) {
			int cur = q.poll();
			str += cur + " ";
			
			for(int node : list.get(cur)) {
				if(!visited[node]) {
					visited[node] = true;
					q.offer(node);
				}
			}
		}
	}
}
