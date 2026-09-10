class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n-1
        s = s.lower()
        while(start<end):
            if s[start].isalnum() and s[end].isalnum():
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            elif not s[start].isalnum():
                start+=1
            else:
                end -= 1
        return True