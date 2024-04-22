import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    static int T;
    static Deque<position> deque = new ArrayDeque<>();

    static class position{
        int x,y,cnt;

        public position(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }

        @Override
        public String toString() {
            return "position{" +
                    "x=" + x +
                    ", y=" + y +
                    ", cnt=" + cnt +
                    '}';
        }
    }

    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        char[][] graph = new char[T][T];
        int[][][] check = new int[T][T][2];

        for(int t=0; t<T; t++) {
            char[] array = br.readLine().toCharArray();
            for (int i = 0; i<array.length; i++) {
                graph[t][i] = array[i];
            }
        }

        for(int i = 0; i<T; i++) {
            for (int j = 0; j<T; j++) {
                if (graph[i][j] == 'B') {
                    deque.add(new position(i, j, 0));
                }
            }
        }


        while (deque.size()!=0) {
            position position = deque.pollFirst();
            int x1 = position.x;
            int y1 = position.y;
            int cnt1 = position.cnt;

            position position1 = deque.pollFirst();
            int x2 = position1.x;
            int y2 = position1.y;
            int cnt2 = position1.cnt;

            position position2 = deque.pollFirst();
            int x3 = position2.x;
            int y3 = position2.y;
            int cnt3 = position2.cnt;

            if (graph[x1][y1] == 'E' && graph[x2][y2] == 'E' && graph[x3][y3] == 'E') {
                answer = Math.min(answer, cnt3);
                continue;
            }


            if (x1 == x2 && x2== x3) {
                check[x2][y2][1] = 1; //가로
            }else{
                check[x2][y2][0] = 1; //세로
            }

            // 오른쪽 이동
            if (y1+1 <T && y2+1<T && y3+1<T) {
                if (graph[x1][y1 + 1] != '1' && graph[x2][y2 + 1] != '1' && graph[x3][y3 + 1] != '1') {
                    if (x1 == x2 && x2 == x3) {
                        if (check[x2][y2+1][1] == 0) {
                            deque.add(new position(x1, y1 + 1, cnt1 + 1));
                            deque.add(new position(x2, y2 + 1, cnt2 + 1));
                            deque.add(new position(x3, y3 + 1, cnt3 + 1));
                            check[x2][y2+1][1] = 1;
                        }
                    }else{
                        if (check[x2][y2+1][0] == 0){
                            deque.add(new position(x1, y1 + 1, cnt1 + 1));
                            deque.add(new position(x2, y2 + 1, cnt2 + 1));
                            deque.add(new position(x3, y3 + 1, cnt3 + 1));
                            check[x2][y2+1][0] = 1;
                        }
                    }
                }
            }

            // 왼쪽 이동
            if (y1-1 >=0 && y2-1>=0 && y3-1>=0) {
                if (graph[x1][y1-1] != '1' && graph[x2][y2-1] != '1' && graph[x3][y3-1]!='1') {
                    if (x1 == x2 && x2 == x3) {
                        if (check[x2][y2 - 1][1] == 0) {
                            deque.add(new position(x1, y1 - 1, cnt1 + 1));
                            deque.add(new position(x2, y2 - 1, cnt2 + 1));
                            deque.add(new position(x3, y3 - 1, cnt3 + 1));
                            check[x2][y2-1][1] = 1;
                        }
                    }
                    else{
                        if (check[x2][y2-1][0] == 0){
                            deque.add(new position(x1, y1 - 1, cnt1 + 1));
                            deque.add(new position(x2, y2 - 1, cnt2 + 1));
                            deque.add(new position(x3, y3 - 1, cnt3 + 1));
                            check[x2][y2-1][0] = 1;
                        }
                    }
                }
            }

            // 위쪽 이동
            if (x1-1 >=0 && x2-1>=0 && x3-1>=0) {
                if (graph[x1-1][y1] != '1' && graph[x2-1][y2] != '1' && graph[x3-1][y3]!='1') {
                    if (x1 == x2 && x2 == x3) {
                        if (check[x2-1][y2][1] == 0) {
                            deque.add(new position(x1-1, y1, cnt1 + 1));
                            deque.add(new position(x2-1, y2, cnt2 + 1));
                            deque.add(new position(x3-1, y3, cnt3 + 1));
                            check[x2-1][y2][1] = 1;
                        }
                    }
                    else{
                        if (check[x2-1][y2][0] == 0){
                            deque.add(new position(x1-1, y1, cnt1 + 1));
                            deque.add(new position(x2-1, y2, cnt2 + 1));
                            deque.add(new position(x3-1, y3, cnt3 + 1));
                            check[x2-1][y2][0] = 1;
                        }
                    }
                }
            }

            // 아래쪽 이동
            if (x1+1 <T && x2+1<T && x3+1<T) {
                if (graph[x1+1][y1] != '1' && graph[x2+1][y2] != '1' && graph[x3+1][y3]!='1') {
                    if (x1 == x2 && x2 == x3) {
                        if (check[x2+1][y2][1] == 0) {
                            deque.add(new position(x1+1, y1, cnt1 + 1));
                            deque.add(new position(x2+1, y2, cnt2 + 1));
                            deque.add(new position(x3+1, y3, cnt3 + 1));
                            check[x2+1][y2][1] = 1;
                        }
                    }
                    else{
                        if (check[x2+1][y2][0] == 0){
                            deque.add(new position(x1+1, y1, cnt1 + 1));
                            deque.add(new position(x2+1, y2, cnt2 + 1));
                            deque.add(new position(x3+1, y3, cnt3 + 1));
                            check[x2+1][y2][0] = 1;
                        }
                    }
                }
            }

            // 회전
            int flag = 0;
            if (x2>0 && x2<T-1 && y2>0 && y2<T-1) {
                for (int x = x2-1; x<=x2+1; x++) {
                    for (int y = y2-1; y<=y2+1; y++) {
                        if (graph[x][y] == '1') {
                            flag = 1;
                            break;
                        }
                    }
                }
                if (flag == 0) {
                    if (x1 == x2 && x2 == x3) {
                        if (check[x2][y2][0] == 0) {
                            deque.add(new position(x2-1, y2, cnt1 + 1));
                            deque.add(new position(x2, y2 , cnt2 + 1));
                            deque.add(new position(x2+1, y2, cnt3 + 1));
                            check[x2][y2][0] = 1;
                        }
                    }
                    else{
                        if (check[x2][y2][1] == 0){
                            deque.add(new position(x2, y2 - 1, cnt1 + 1));
                            deque.add(new position(x2, y2, cnt2 + 1));
                            deque.add(new position(x2, y2 + 1, cnt3 + 1));
                            check[x2][y2][1] = 1;
                        }
                    }
                }
            }
        }

        if (answer == Integer.MAX_VALUE) {
            System.out.println(0);
        }
        else {
            System.out.println(answer);
        }
    }
}