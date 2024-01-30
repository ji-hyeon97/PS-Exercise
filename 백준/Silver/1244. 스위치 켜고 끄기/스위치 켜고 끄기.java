import java.util.Scanner;

public class Main {
    static int[] switchArr;

    public static void change(int num) {
        if (switchArr[num] == 0) {
            switchArr[num] = 1;
        } else {
            switchArr[num] = 0;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        switchArr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            switchArr[i] = scanner.nextInt();
        }

        int students = scanner.nextInt();
        for (int s = 0; s < students; s++) {
            int sex = scanner.nextInt();
            int num = scanner.nextInt();
            if (sex == 1) {
                for (int i = num; i <= N; i += num) {
                    change(i);
                }
            }
            else {
                change(num);
                for (int k = 0; k < N / 2; k++) {
                    if (num + k > N || num - k < 1) {
                        break;
                    }
                    if (switchArr[num + k] == switchArr[num - k]) {
                        change(num + k);
                        change(num - k);
                    } else {
                        break;
                    }
                }
            }
        }
        for (int i = 1; i <= N; i++) {
            System.out.print(switchArr[i] + " ");
            if (i % 20 == 0) {
                System.out.println();
            }
        }
        scanner.close();
    }
}