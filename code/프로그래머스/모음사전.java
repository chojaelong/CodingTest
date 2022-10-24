public class 모음사전 {
    StringBuilder words = new StringBuilder();
    int answer = 0;
    boolean find = false;
    String[] array = new String[]{"A", "E", "I", "O", "U"};
    
    public void back_tracking(String word) {
        int length = words.length();
        
        if (length >= 5)
            return;
            
        for(String w : array) {
            words.append(w);
            answer += 1;
            if (word.equals(words.toString())) {
                find = true;
                return;
            }
            back_tracking(word);
            if (find) {
                return;
            }
            words.deleteCharAt(length - 1);
            
        }
    }
    
    public int solution(String word) {
        back_tracking(word);
        return answer;
    }
}
