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
        int jimin = Integer.parseInt(st.nextToken());
        int hansu = Integer.parseInt(st.nextToken());
        int count = 0;

        while (true){
            if (jimin == hansu){
                break;
            }

            if (jimin%2 == 1){
                jimin = (int) (Math.floor(jimin/2) + 1);
            }
            else{
                jimin/=2;
            }

            if (hansu%2 == 1){
                hansu = (int) (Math.floor(hansu/2) + 1);
            }
            else{
                hansu/=2;
            }
            count+=1;
        }
        System.out.println(count);
    }
}