import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static int r, c;
    static char[][] graph;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static HashMap<Character, Integer> dic = new HashMap<>();
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        graph = new char[r][c];

        for (int i = 0; i < r; i++) {
            String data = br.readLine();
            graph[i] = data.toCharArray();
        }

        dic.put(graph[0][0], 1);
        dfs(0, 0, 1);
        System.out.println(answer);
    }

    static void dfs(int x, int y, int cnt) {
        answer = Math.max(answer, cnt);
        for (int i = 0; i < 4; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                if (!dic.containsKey(graph[nx][ny])) {
                    dic.put(graph[nx][ny], 1);
                    dfs(nx, ny, cnt + 1);
                    dic.remove(graph[nx][ny]);
                }
            }
        }
    }
}