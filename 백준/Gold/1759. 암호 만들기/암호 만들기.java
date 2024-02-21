
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static int l, c;
    static String[] data;
    static int[] temp;
    static int[] check;
    static List<Integer> password;
    static char[] vowel = {'a', 'e', 'i', 'o', 'u'};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] lc = br.readLine().split(" ");
        l = Integer.parseInt(lc[0]);
        c = Integer.parseInt(lc[1]);

        data = br.readLine().split(" ");
        temp = new int[c];
        for (int i = 0; i < c; i++) {
            temp[i] = (int) data[i].charAt(0);
        }

        Arrays.sort(temp);
        check = new int[200];
        password = new ArrayList<>();
        backtracking(0);
    }

    public static void backtracking(int index) {
        if (password.size() == l) {
            StringBuilder answer = new StringBuilder();
            int alphabet_vowel = 0;
            int alphabet_consonant = 0;
            for (int i : password) {
                if (isVowel((char) i)) {
                    alphabet_vowel++;
                } else {
                    alphabet_consonant++;
                }
            }
            if (alphabet_consonant >= 2 && alphabet_vowel >= 1) {
                for (int i : password) {
                    answer.append((char) i);
                }
                System.out.println(answer);
            }
            return;
        }

        for (int i = index; i < c; i++) {
            password.add(temp[i]);
            backtracking(i + 1);
            password.remove(password.size() - 1);
        }
    }

    public static boolean isVowel(char c) {
        for (char v : vowel) {
            if (c == v) return true;
        }
        return false;
    }
}