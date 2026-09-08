class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        mp = {}
        ans = []
        for n in nums:
            if n not in mp:
                mp[n] = 0
            mp[n] += 1

        for key, value in mp.items():
            freq[value].append(key)
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            for x in freq[i]:
                if k<= 0:
                    return ans
                ans.append(x)
                k -= 1

        return ans
                

        # mp = {}
        # ans = []
        # for n in nums:
        #     if n not in mp:
        #         mp[n] = 0
        #     mp[n] += 1
        
        # mp = sorted(mp.items(), key =  lambda x:x[1], reverse  = True)
        # for key in mp:
        #     if k>0:
        #         ans.append(key[0])
        #         k -= 1
        #     else:
        #         break
        # return ans