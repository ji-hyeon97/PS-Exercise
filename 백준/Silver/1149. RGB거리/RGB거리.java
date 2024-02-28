import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[] r;
	static int[] g;
	static int[] b;
	
	static int[][] data;
	
	public static void main(String[] args) throws Exception, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		r = new int[N+3];
		g = new int[N+3];
		b = new int[N+3];
		data = new int[N+3][4];
		for(int i = 1; i<N+1; i++) {
			st = new StringTokenizer(br.readLine());
			r[i] = Integer.parseInt(st.nextToken());
			g[i] = Integer.parseInt(st.nextToken());
			b[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 1; i<N+1; i++) {
			data[i][0] = Math.min(data[i-1][1], data[i-1][2]) + r[i];
			data[i][1] = Math.min(data[i-1][0], data[i-1][2]) + g[i];
			data[i][2] = Math.min(data[i-1][0], data[i-1][1]) + b[i];
			
		}
		
		int min = Math.min(Math.min(data[N][0], data[N][1]), data[N][2]);
        System.out.println(min);
	}
}