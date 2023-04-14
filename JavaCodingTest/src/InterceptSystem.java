import java.util.*;
public class InterceptSystem {

    public static void main(String[] args) {

    }

    public int solution(int[][] targets) {
        int length = targets.length;
        boolean[] visited = new boolean[length];
        int[] cover = new int[100000001];
        Arrays.fill(visited, false);
        System.out.println(Arrays.toString(visited));

        for (int i = 0; i < length; i++) {
            int start = targets[i][0];
            int end = targets[i][1];

            for (int j = start; j <= end; j++) {
                cover[j]++;
            }
        }

        int count = 0;
        boolean[] want = new boolean[length];

        int answer = 0;
        return answer;
    }
}
