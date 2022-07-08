import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 수들의합 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(reader.readLine());
        ArrayList<Long> dp = new ArrayList<>();
        dp.add(0l);
        dp.add(1l);

        int i = 2;
        
        while(true){
            long value = dp.get(i-1) + i;
            dp.add(value);

            if(value > n){
                break;
            }

            i++;
        }

        System.out.println(i - 1);
    }
}