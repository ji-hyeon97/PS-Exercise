import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    static char[][] map;
    static int[][] check;
    static Deque<Position> fire;
    static Deque<Position> human;
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,1,0,-1};
    static int h,w;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for(int t=0; t<T; t++){
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            map = new char[h][w];
            check = new int[h][w];
            fire = new ArrayDeque<>();
            human = new ArrayDeque<>();
            count = Integer.MAX_VALUE;

            for(int i = 0; i<h; i++){
                String data = br.readLine();
                for(int j = 0; j<w; j++){
                    map[i][j] = data.charAt(j);
                    if ('*' == map[i][j]){
                        fire.add(new Position(i,j,0));
                        check[i][j] = 1;
                    }
                    if ('@' == map[i][j]){
                        human.add(new Position(i,j,0));
                    }
                }
            }

            fireSpread();
            humanRun();

            if (count == Integer.MAX_VALUE){
                System.out.println("IMPOSSIBLE");
            }
            else{
                System.out.println(count);
            }
        }
    }

    private static void humanRun(){
        while (human.size()!=0){
            Position position = human.pollFirst();
            for(int i= 0; i<4; i++){
                int nx = position.x + dx[i];
                int ny = position.y + dy[i];

                if (nx>=0 && nx<h && ny>=0 && ny<w){
                    if (map[nx][ny] == '#'){
                        continue;
                    }

                    if (map[nx][ny] == '*'){
                        continue;
                    }

                    if (map[nx][ny] == '@'){
                        continue;
                    }

                    if (map[nx][ny] == '.' && check[nx][ny] == 0){
                        human.add(new Position(nx,ny, position.count+1));
                        check[nx][ny] = position.count;
                        continue;
                    }

                    if (map[nx][ny] == '.' && check[nx][ny] > position.count+1){
                        human.add(new Position(nx,ny, position.count+1));
                        check[nx][ny] = position.count;
                    }
                }
                else{
                    count = Math.min(count,position.count+1);
                }
            }
        }
    }

    private static void fireSpread(){
        while (fire.size()!=0){
            Position position = fire.pollFirst();
            for(int i= 0; i<4; i++){
                int nx = position.x + dx[i];
                int ny = position.y + dy[i];

                if (nx>=0 && nx<h && ny>=0 && ny<w){
                    if (map[nx][ny] == '#'){
                        continue;
                    }

                    if (map[nx][ny] == '*'){
                        continue;
                    }

                    if (map[nx][ny] == '@' && check[nx][ny] == 0){
                        fire.add(new Position(nx,ny, position.count+1));
                        check[nx][ny] = position.count+1;
                    }

                    if (map[nx][ny] == '.' && check[nx][ny] == 0){
                        fire.add(new Position(nx,ny, position.count+1));
                        check[nx][ny] = position.count+1;
                    }
                }
            }
        }
    }

    private static class Position{
        int x;
        int y;
        int count;

        public Position(int x, int y, int count) {
            this.x = x;
            this.y = y;
            this.count = count;
        }
    }
}