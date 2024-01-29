import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for(int i = 1; i<=t; i++) {
			String data = br.readLine();
			char[] temp = data.toCharArray();
			int count = 0;
			int index = 0;
			while (true) {
				if (index == temp.length) {
					break;
				}
				if ('0' == temp[index]) {
					index++;
					continue;
				}
				for(int j = index; j<data.length(); j++) {
					if ('1' == temp[j]) {
						temp[j] = '0';
					}else {
						temp[j] = '1';
					}
				}
				count++;
				index++;
			}
			System.out.println("#"+i+" "+count);
		}
	}
}