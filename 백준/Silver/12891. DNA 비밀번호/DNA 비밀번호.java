import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Character> queue = new ArrayDeque<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[] data = br.readLine().toCharArray();
        int[] cnt = new int[4];
        StringTokenizer cntTokens = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            cnt[i] = Integer.parseInt(cntTokens.nextToken());
        }

        int answer = 0;
        Map<Character, Integer> dic = new HashMap<>();
        dic.put('A', 0);
        dic.put('C', 0);
        dic.put('G', 0);
        dic.put('T', 0);

        for (int i = 0; i <= data.length; i++) {
            if (queue.size() == m) {
                if (dic.get('A') >= cnt[0] && dic.get('C') >= cnt[1] && dic.get('G') >= cnt[2] && dic.get('T') >= cnt[3]) {
                    answer++;
                    dic.put(queue.peekFirst(), dic.get(queue.peekFirst()) - 1);
                    queue.pollFirst();
                } else {
                    dic.put(queue.peekFirst(), dic.get(queue.peekFirst()) - 1);
                    queue.pollFirst();
                }
            }
            if (i == data.length) {
                continue;
            }
            queue.offerLast(data[i]);
            dic.put(data[i], dic.get(data[i]) + 1);
        }
        System.out.println(answer);
    }
}