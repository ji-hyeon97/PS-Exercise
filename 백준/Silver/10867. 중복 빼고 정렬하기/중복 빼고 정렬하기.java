import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;


public class Main {

    static Set set;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        set = new TreeSet();

        for(int i = 0; i<N; i++){
            set.add(Integer.parseInt(st.nextToken()));
        }

        Iterator iter = set.iterator();
        while(iter.hasNext()){
            System.out.print(iter.next() + " ");
        }
    }
}