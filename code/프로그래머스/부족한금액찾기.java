class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long s = 0;
        
        for (int i = 1; i < count + 1; i++)
        {
            s = s + (price * i);
        }

        if(s > money){
            return s - money;
        }
        return 0;
    }
}