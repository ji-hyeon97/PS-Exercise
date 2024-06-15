import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for(int t = 1; t<=T; t++){
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int count = 1;
            int total = (1<<10)-1;
            int check = 0;
            while (true){

                if (check == total){
                    System.out.println("#"+t+" " +(N*(count-1)));
                    break;
                }

                String number = String.valueOf(N*count);

                for(int i = 0; i<number.length(); i++){
                    int c = Integer.parseInt(String.valueOf(number.charAt(i)));
                    check = check | (1<<c);
                }
                count+=1;
            }
        }
    }
}