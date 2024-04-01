import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
    static class Point {
        int x, y, times;

        Point(int x, int y, int times) {
            this.x = x;
            this.y = y;
            this.times = times;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int n = Integer.parseInt(br.readLine());
            int[][] graph = new int[n][n];

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            StringTokenizer startCoords = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(startCoords.nextToken());
            int startY = Integer.parseInt(startCoords.nextToken());

            StringTokenizer endCoords = new StringTokenizer(br.readLine());
            int endX = Integer.parseInt(endCoords.nextToken());
            int endY = Integer.parseInt(endCoords.nextToken());

            Queue<Point> queue = new ArrayDeque<>();
            queue.offer(new Point(startX, startY, 0));

            boolean[][] check = new boolean[n][n];
            check[startX][startY] = true;
            int answer = Integer.MAX_VALUE;

            int[] dx = {-1, 0, 1, 0};
            int[] dy = {0, 1, 0, -1};

            while (!queue.isEmpty()) {
                Point point = queue.poll();
                int x = point.x;
                int y = point.y;
                int times = point.times;

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= n || ny >= n)
                        continue;
                    if (nx == endX && ny == endY) {
                        answer = Math.min(answer, times + 1);
                        continue;
                    }
                    if (graph[nx][ny] == 1)
                        continue;
                    if ((times + 1) % 3 == 0 && graph[nx][ny] == 2 && !check[nx][ny]) {
                        check[nx][ny] = true;
                        queue.offer(new Point(nx, ny, times + 1));
                    }
                    if ((times + 1) % 3 != 0 && graph[nx][ny] == 2 && !check[nx][ny]) {
                        queue.offer(new Point(x, y, times + 1));
                    }
                    if (graph[nx][ny] == 0 && !check[nx][ny]) {
                        queue.offer(new Point(nx, ny, times + 1));
                        check[nx][ny] = true;
                    }
                }
            }
            if (answer == Integer.MAX_VALUE)
                System.out.println("#" + t + " " + -1);
            else
                System.out.println("#" + t + " " + answer);
        }
        br.close();
    }
}