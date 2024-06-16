import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int count = 0;
        map = new int[N+3];

        for(int i = 2; i<=N; i++){
            map[i] = 1;
        }

        while (true){

            int flag = 0;
            int target = 0;
            for(int i = 2; i<=N; i++){
                if (map[i] == 1){
                    target = i;
                    break;
                }
            }

            for(int i = 1; i*target<=N; i++){
                if (map[i*target] == 1){
                    count+=1;
                    map[i*target] = 0;
                    if (count == M){
                        System.out.println(i*target);
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag == 1){
                break;
            }
        }
    }
}