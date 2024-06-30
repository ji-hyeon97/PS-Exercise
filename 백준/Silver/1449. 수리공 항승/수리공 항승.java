import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int L;
    static int[] water;
    static int[] check = new int[2005];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        water = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i<N; i++){
            water[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(water);
        int answer = 0;

        for(int i : water){
            if (check[i] == 0){
                answer+=1;
                for(int j = i; j<i+L; j++){
                    check[j] = 1;
                }
            }
        }
        System.out.println(answer);
    }
}