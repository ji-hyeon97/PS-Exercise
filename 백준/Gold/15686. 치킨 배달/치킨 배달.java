import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static int[][] graph;
    static List<int[]> home;
    static List<int[]> chicken;
    static int answer = (int) 1e9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][n];
        home = new ArrayList<>();
        chicken = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) {
                    home.add(new int[]{i, j});
                }
                if (graph[i][j] == 2) {
                    chicken.add(new int[]{i, j});
                }
            }
        }

        recur(0, new ArrayList<>());
        System.out.println(answer);
    }

    static void recur(int depth, List<int[]> list) {
        if (depth == chicken.size()) {
            if (list.size() == m) {
                answer = Math.min(answer, cal(list));
            }
            return;
        }
        recur(depth + 1, list);
        List<int[]> newList = new ArrayList<>(list);
        newList.add(chicken.get(depth));
        recur(depth + 1, newList);
    }

    static int cal(List<int[]> list) {
        int distance = 0;
        for (int[] h : home) {
            int temp = (int) 1e9;
            for (int[] c : list) {
                temp = Math.min(temp, Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1]));
            }
            distance += temp;
        }
        return distance;
    }
}