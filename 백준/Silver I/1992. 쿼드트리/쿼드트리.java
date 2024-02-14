import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static char[][] graph;
	static int n;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		graph = new char[n][];
		for (int t = 0; t<n; t++) {
			graph[t] = br.readLine().toCharArray();
		}
		
		sol(0,0,n);
	}
	
	public static void sol(int x,int y,int n) {
		char target = graph[x][y];
		for (int i = x; i<x+n; i++) {
			for(int j = y; j<y+n; j++) {
				if (graph[i][j] != target) {
					target = '*';
					break;
				}
			}
		}
		if (target == '*') {
			n = n/2;
			System.out.print("(");
			sol(x,y,n);
			sol(x,y+n,n);
			sol(x+n,y,n);
			sol(x+n,y+n,n);
			System.out.print(")");
		}
		if (target == '1') {
			System.out.print("1");
		}
		if (target == '0') {
			System.out.print("0");
		}
	}
}