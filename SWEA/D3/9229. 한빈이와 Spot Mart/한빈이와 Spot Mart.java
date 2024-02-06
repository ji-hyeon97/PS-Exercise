import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int[] snacks;
    static int answer;
    static int n;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case<T+1; test_case++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            snacks = new int[n];
            answer = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i<n; i++) {
                snacks[i] = Integer.parseInt(st.nextToken());
            }
            recur(0,0,m,0);
            if (answer == 0) {
                System.out.println("#"+test_case+" "+-1);
                continue;
            }
            System.out.println("#"+test_case+" "+answer);
        }
    }
    static void recur(int node, int temp,int m, int cnt) {

        if (temp>m) {
            return;
        }
        if (cnt == 2) {
            answer = Math.max(answer, temp);
            return;
        }
        if(node == n ){
            return;
        }
        recur(node+1,temp,m,cnt);
        recur(node+1,temp+snacks[node],m,cnt+1);
    }
}