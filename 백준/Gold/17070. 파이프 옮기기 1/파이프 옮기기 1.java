import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[][] graph;
    static int[] dx = {1, 0, 1};
    static int[] dy = {0, 1, 1};
    static Queue<Point> queue = new ArrayDeque<>();
    static int answer = 0;

    static class Point {
        int x, y, kind;

        Point(int x, int y, int kind) {
            this.x = x;
            this.y = y;
            this.kind = kind;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        queue.add(new Point(0, 1, 1));

        if (graph[n - 1][n - 1] == 1) {
            bw.write("0\n");
            bw.flush();
            return;
        }

        bfs();
        bw.write(answer + "\n");
        bw.flush();
    }

    static void bfs() {
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            int x = point.x;
            int y = point.y;
            int kind = point.kind;

            if (x == n - 1 && y == n - 1) {
                answer++;
                continue;
            }

            if (kind == 0) {
                for (int i : new int[]{0, 2}) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                        continue;
                    }

                    if (graph[nx][ny] != 0) {
                        continue;
                    }

                    if (graph[nx][ny] == 0) {
                        if (i == 2) {
                            if(graph[x + 1][y] == 0 && graph[x][y + 1] == 0) {
                                queue.add(new Point(nx, ny, i));
                            }
                        } else {
                            queue.add(new Point(nx, ny, i));
                        }
                    }
                }
            }

            if (kind == 1) {
                for (int i : new int[]{1, 2}) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                        continue;
                    }

                    if (graph[nx][ny] != 0) {
                        continue;
                    }

                    if (graph[nx][ny] == 0) {
                        if (i == 2) {
                            if(graph[x + 1][y] == 0 && graph[x][y + 1] == 0) {
                                queue.add(new Point(nx, ny, i));
                            }
                        } else {
                            queue.add(new Point(nx, ny, i));
                        }
                    }
                }
            }

            if (kind == 2) {
                for (int i : new int[]{0, 1, 2}) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                        continue;
                    }

                    if (graph[nx][ny] != 0) {
                        continue;
                    }

                    if (graph[nx][ny] == 0) {
                        if (i == 0 || i == 1) {
                            queue.add(new Point(nx, ny, i));
                        } else {
                            if (graph[x + 1][y] == 0 && graph[x][y + 1] == 0) {
                                queue.add(new Point(nx, ny, i));
                            }
                        }
                    }
                }
            }
        }
    }
}