
import java.io.*;
public class Main
{
    //1 ≤ k 층, n ≤ 14 호
    static int[][] dp = new int [15][15];
    static int T, K, N;
    static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    T = Integer.parseInt(br.readLine());
	    for(int i=0; i<15; i++){
	        
	        for(int j=1; j<15; j++){
	            if(i==0) dp[i][j] = j;
	            else dp[i][j] = dp[i][j-1] + dp[i-1][j];
	        }
	    }
	    
	    
	    for(int t=1; t<=T; t++){
	       K = Integer.parseInt(br.readLine());
	       N = Integer.parseInt(br.readLine());
	       sb.append(dp[K][N]).append("\n");
	    }
	    System.out.println(sb);
	    br.close();
	    
	}
}
