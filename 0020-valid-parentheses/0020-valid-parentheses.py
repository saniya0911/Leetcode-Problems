class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            elif ch in brackets.keys():
                if stack:
                    last = stack.pop()
                    if brackets[ch] != last:
                        return False
                else:
                    return False

        if not stack:
            return True
        else:
            return False