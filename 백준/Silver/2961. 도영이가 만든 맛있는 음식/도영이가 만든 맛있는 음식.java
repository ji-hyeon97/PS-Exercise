import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int answer = Integer.MAX_VALUE;
	static int[][] menu;
	static int t;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		t = Integer.parseInt(st.nextToken());
		menu = new int[t][22];
		
		for (int i = 0; i<t; i++) {
			st = new StringTokenizer(br.readLine());
			menu[i][0] = Integer.parseInt(st.nextToken());
			menu[i][1] = Integer.parseInt(st.nextToken());
		}
		
		recur(1,0,0,0);
		System.out.println(answer);
	}
	public static void recur(int start, int end, int idx, int flag) {
		
		if (idx == t) {
			if (flag == 0) {
				return;
			}
			answer = Math.min(answer, Math.abs(end-start));
			return;
		}
		
		recur(start, end, idx+1,flag);
		recur(start*menu[idx][0], end+menu[idx][1], idx+1,flag+1);
	}
}