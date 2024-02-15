import java.util.Scanner;

public class Solution {
    static char[] cmdDirList = {'U', 'D', 'L', 'R'};
    static int[][] drcList = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static char[] directionList = {'^', 'v', '<', '>'};

    static class Tank {
        int r, c;
        char direction;

        public Tank(int r, int c, char direction) {
            this.r = r;
            this.c = c;
            this.direction = direction;
        }
    }

    static Tank findMe(char[][] field, int H, int W) {
        for (int r = 0; r < H; r++) {
            for (int c = 0; c < W; c++) {
                for (int i = 0; i < 4; i++) {
                    if (field[r][c] == directionList[i]) {
                        return new Tank(r, c, directionList[i]);
                    }
                }
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int H = scanner.nextInt();
            int W = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            char[][] field = new char[H][W];

            for (int i = 0; i < H; i++) {
                field[i] = scanner.nextLine().toCharArray();
            }

            int N = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            char[] cmdList = scanner.nextLine().toCharArray();

            Tank me = findMe(field, H, W);

            for (char cmd : cmdList) {
                if (cmd == 'S') { // Shoot
                    int bombIdx = -1;
                    for (int i = 0; i < 4; i++) {
                        if (me.direction == directionList[i]) {
                            bombIdx = i;
                            break;
                        }
                    }
                    int b_r = drcList[bombIdx][0];
                    int b_c = drcList[bombIdx][1];
                    int bomb_r = me.r;
                    int bomb_c = me.c;

                    while (bomb_r >= 0 && bomb_r < H && bomb_c >= 0 && bomb_c < W) {
                        if (field[bomb_r][bomb_c] == '#') {
                            break;
                        }

                        if (field[bomb_r][bomb_c] == '*') {
                            field[bomb_r][bomb_c] = '.';
                            break;
                        }

                        bomb_r += b_r;
                        bomb_c += b_c;
                    }

                } else { // Move
                    int meIdx = -1;
                    for (int i = 0; i < 4; i++) {
                        if (cmd == cmdDirList[i]) {
                            meIdx = i;
                            break;
                        }
                    }
                    int r = drcList[meIdx][0];
                    int c = drcList[meIdx][1];
                    char newDirection = directionList[meIdx];

                    if (me.r + r >= 0 && me.r + r < H && me.c + c >= 0 && me.c + c < W && field[me.r + r][me.c + c] == '.') {
                        field[me.r][me.c] = '.';
                        me.r += r;
                        me.c += c;
                    }
                    me.direction = newDirection;
                    field[me.r][me.c] = newDirection;
                }
            }

            System.out.print("#" + tc + " ");
            for (char[] row : field) {
                System.out.println(row);
            }
        }

        scanner.close();
    }
}