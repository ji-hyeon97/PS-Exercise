import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<Integer> seq = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .boxed()
                .collect(Collectors.toList());

        int max = 0;
        double sum = 0;

        for (int i:seq){
            if (i>max) {
                max = i;
            }
            sum+=i;
        }
        System.out.println(((sum / max) * 100.0) / n);
    }
}