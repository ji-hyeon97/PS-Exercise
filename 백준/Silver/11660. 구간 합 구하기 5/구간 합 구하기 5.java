import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		arr = new int[n][n];
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j<n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++) {
				if (i==0 && j ==0) {
					continue;
				}
				if (i>0 && j == 0) {
					arr[i][j] += arr[i-1][j];
				}
				if (i==0 && j>0) {
					arr[i][j] += arr[i][j-1];
				}
				if (i>0 && j>0) {
					arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1];
				}
			}
		}
		for (int i = 0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			x1-=1;
			x2-=1;
			y1-=1;
			y2-=1;
			int answer = 0;
			
			if (x1 > 0 && y1 > 0) {
				answer = arr[x2][y2] - arr[x2][y1 - 1] - arr[x1 - 1][y2] + arr[x1 - 1][y1 - 1];
			}
			if (x1 > 0 && y1 == 0) {
				answer = arr[x2][y2] - arr[x1 - 1][y2];
			}
			if (x1 == 0 && y1 > 0) {
				answer = arr[x2][y2] - arr[x2][y1 - 1];
			}
			if (x1 == 0 && y1 == 0) {
				answer = arr[x2][y2];
			}
			
			System.out.println(answer);
		}
	}
}