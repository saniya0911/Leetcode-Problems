class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int free =0;
        int size = flowerbed.length;
        for(int i=0;i<size;i++)
        {
            if(flowerbed[i]==1)
            {
                i++;
                continue;
            }
            else if(i!=size-1 && flowerbed[i+1]==1)
            continue;
            else 
            {
                free++;
                i++;
            }
        }
        if(free>=n)
        return true;
        else
        return false;
    }
}