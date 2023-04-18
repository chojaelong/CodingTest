import java.util.*;
public class Keyboard {

    public static void main(String[] args) {

    }

    public int[] solution(String[] keymap, String[] targets) {
        Map<String, Integer> map = new HashMap<>();

        for (String key : keymap) {
            for (int i = 0; i < key.length(); i++) {
                String s = Character.toString(key.charAt(i));
                if (!map.containsKey(s)) {
                    map.put(s, i);
                }
            }
        }


        int[] answer = {};
        return answer;
    }
}
