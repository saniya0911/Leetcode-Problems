class Solution {
    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> list=new ArrayList<>();
        int k=0;
        for(int i=0;i<nums.length;i++)
        {
            if(i!=nums.length-1 && nums[i]==nums[i+1])
               continue;
            k++;
            list.add(nums[i]);
        }
        for(int i=0;i<k;i++)
        nums[i]=list.get(i);

        return k;
    }
}