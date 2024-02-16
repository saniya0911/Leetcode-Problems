class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        HashMap<Integer,Integer> frequency = new HashMap<>();
        int n= arr.length;
        for(int i=0;i<n;i++)
        {
            if(frequency.containsKey(arr[i]))
            frequency.put(arr[i],frequency.get(arr[i])+1);
            else
            frequency.put(arr[i],1);
        }
        //sort(frequency);
        ArrayList<Integer> fre = new ArrayList<>();
        for(Map.Entry<Integer,Integer> e : frequency.entrySet())
        {
            fre.add(e.getValue());
        }
        Collections.sort(fre);
        int i=0;
        for(i=0;i<fre.size();i++)
        {
            if(k>=fre.get(i))
            k-=fre.get(i);
            else
            break;
        }
        return (fre.size()-i);
    }
}
    