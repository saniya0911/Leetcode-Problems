class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] * (len(s)+1)
        return self.issegment(0, s, wordDict, dp)
    
    def issegment(self, start, s, wordDict, dp):
        if not dp[start]:
            return False
        if(start == len(s)):
            return True
        
        for i in range(start+1, len(s)+1):
            if s[start: i] in wordDict and self.issegment(i, s, wordDict, dp):
                return True

        dp[start] = False
        return False