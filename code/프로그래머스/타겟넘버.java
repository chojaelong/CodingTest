import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    int count = 0;
    public int solution(int[] numbers, int target) {
        boolean[] visited = new boolean[numbers.length];
        Arrays.fill(visited, false);
        
        dfs(numbers, visited, 0, target);
        
        return count;        
    }
    
    public void dfs(int[] numbers, boolean[] visited, int i, int target) {
        if (i < numbers.length){
            visited[i] = true;
            dfs(numbers, visited, i + 1, target);
            numbers[i] = -numbers[i];
            dfs(numbers, visited, i + 1, target);
        }
        else if (i == numbers.length){
            int sum = 0;
            for (int num : numbers){
                sum += num;
            }
            
            if (sum == target){
                count++;
            }
        }
    }
}