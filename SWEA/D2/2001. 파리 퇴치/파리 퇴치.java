import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution{

    static int[][] graph;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case<T+1; test_case++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int answer = 0;
            graph = new int[n][n];
            for (int a = 0; a<n; a++){
                st = new StringTokenizer(br.readLine());
                for (int b = 0; b<n; b++){
                    graph[a][b] = Integer.parseInt(st.nextToken());
                }
            }
            for (int i =0; i<n-(m-1); i++){
                for (int j = 0; j<n-(m-1); j++){
                    int temp = 0;
                    for (int k = i; k<i+m; k++){
                        for (int t = j; t<j+m; t++){
                            temp+=graph[k][t];
                        }
                    }
                    answer = Math.max(answer,temp);
                }
            }
            System.out.println("#"+test_case+" "+answer);
        }
    }
}