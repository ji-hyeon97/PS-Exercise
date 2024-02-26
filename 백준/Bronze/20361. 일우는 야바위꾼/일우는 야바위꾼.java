import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[] arr;
	public static void main(String[] args) throws Exception, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		arr = new int[N+1];
		arr[X] = 1;
		for(int k = 0; k<K; k++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
				
			swap(from, to);
		}
			
		int index = -1;
		for (int i =0; i<N+1; i++) {
			if (arr[i] == 1) {
				index = i;
			}
		}
		
		System.out.println(index);
	}
	
	
	static void swap(int from, int to) {
		int temp = arr[from];
		arr[from] = arr[to];
		arr[to] = temp;
	}
}