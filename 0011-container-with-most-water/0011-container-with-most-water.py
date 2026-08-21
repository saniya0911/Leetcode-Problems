class Solution:
    def maxArea(self, height: List[int]) -> int:
        total_max = 0
        currmax = 0
        left = 0
        right = len(height) -1
        while(left <= right):
            currmax = min(height[left], height[right]) * (right - left)
            total_max = max(total_max, currmax)
            if(height[left] < height[right]):
                left +=1
            elif(height[left] > height[right]):
                right -= 1
            else:
                left += 1
                right -=1
        return total_max