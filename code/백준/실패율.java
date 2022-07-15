import java.util.Arrays;

class 실패율 {
    public static void main(String[] args) {
        solution(5, new int[] {2, 1, 2, 6, 2, 4, 3, 3});
    }
    public static int[] solution(int N, int[] stages) {
        int[] last_stage = new int[N+2];
        int[] not_clear_stage = new int[N+1];
        double[] fail = new double[N+1];
        for (int stage : stages){
            for (int i = 1; i < stage + 1; i++){
                last_stage[i]++;
            }
        }
        
        for (int i = 1; i < not_clear_stage.length; i++){
            not_clear_stage[i] = last_stage[i] - last_stage[i+1];
            if (last_stage[i] == 0){
                fail[i] = 0d;
            }
            else{
                fail[i] = Double.valueOf(not_clear_stage[i]) / Double.valueOf(last_stage[i]);
            }
        }
        
        int[] answer = new int[N];
        boolean[] searched_index = new boolean[N+1];
        Arrays.fill(searched_index, Boolean.FALSE);
        searched_index[0] = true;
        
        for (int i = 0; i < N; i++){
            int max_index = -1;
            double max_value = -1d;
            for (int j = 1; j < fail.length; j++){
                if (!searched_index[j]){
                    if (max_value < fail[j]){
                        max_value = fail[j];
                        max_index = j;
                    }
                }
            }
            answer[i] = max_index;
            searched_index[max_index] = true;
        }
        
        return answer;
    }
}