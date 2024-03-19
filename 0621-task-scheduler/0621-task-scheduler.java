class Solution {
    public int leastInterval(char[] tasks, int n) {
        int freq[] = new int[26];
        for(char task: tasks)
        {
            freq[task-'A']++;
        }
        Arrays.sort(freq);
        int fre = freq[25];
        int vacant = --fre * n;
        for(int i =24;i>=0;i--)
        {
            vacant-=Math.min(freq[i], fre);
        }
        return vacant>0?tasks.length+vacant : tasks.length;
    }
}