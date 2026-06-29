class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.length;
        for(int i = 0; i< len; i++)
        {
            if(flowerbed[i] == 1 || (i-1 >= 0 && flowerbed[i-1] == 1) || (i+1 < len && flowerbed[i+1] ==1))
            {
                continue;
            }
            else
            {
                flowerbed[i] = 1;
                n--;
            }
        }
        if(n<=0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}