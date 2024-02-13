import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static int N;
	static int[] dp = new int[5001];
	static int INF = 987654321;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		dp[0] = INF;
		dp[1] = INF;
		dp[2] = INF;
		dp[3] = 1;
		dp[4] = INF;
		dp[5] = 1;
		dp[6] = 2;

		for (int i = 7; i <= N; i++) {
			if(dp[i-3] == INF && dp[i-5] == INF)
				dp[i] = INF;
			else {
				if(dp[i-3] != INF) dp[i] = dp[i-3] + 1 ;
				if(dp[i-5] != INF) dp[i] = dp[i-5] + 1 ;
			}
		}

		if (dp[N] == INF)
			System.out.println("-1");
		else
			System.out.println(dp[N]);
	}

}
