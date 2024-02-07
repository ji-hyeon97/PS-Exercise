import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] arr;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		arr = new int[100][100];
		
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			for(int j = a; j<a+10; j++) {
				for (int k = b; k<b+10; k++) {
					arr[j][k] = 1;
				}
			}
		}
		
		int answer = 0;
		for (int i = 0; i<100; i++) {
			for(int j = 0; j<100; j++) {
				if (arr[i][j] == 1) {
					answer+=1;
				}
			}
		}
		System.out.println(answer);
	}
}