class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        for n in nums:
            if n not in mp:
                mp[n] = 0
            mp[n] += 1
        
        mp = sorted(mp.items(), key =  lambda x:x[1], reverse  = True)
        for key in mp:
            if k>0:
                ans.append(key[0])
                k -= 1
            else:
                break
        return ans