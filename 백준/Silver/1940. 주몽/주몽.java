import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int[] map;
    static int N,M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        map = new int[N];

        for(int i = 0; i<N; i++){
            map[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(map);

        int left = 0;
        int right = N-1;
        int answer = 0;
        while (true){
            if (left>= right){
                break;
            }

            if (map[left] + map[right] > M){
                right-=1;
                continue;
            }

            if (map[left] + map[right] < M){
                left+=1;
                continue;
            }

            if(map[left] + map[right] == M){
                answer+=1;
                left+=1;
            }
        }
        System.out.println(answer);
    }
}