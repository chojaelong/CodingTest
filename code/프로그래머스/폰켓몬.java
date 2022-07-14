import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.Arrays;

class 폰켓몬 {   
    public static int solution(int[] nums) {
        int pick = nums.length / 2;
        int kind = Arrays.stream(nums).distinct().toArray().length;
        
        if (kind > pick)
            return pick;
        else
            return kind;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[] {3,1,2,3})); 
    }
}