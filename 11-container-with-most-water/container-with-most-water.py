class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        max_so_far = 0
    
        while front <= back:
            area = (min(height[front],  height[back]) * (back - front))

            if height[front] <= height[back]:
                front += 1
            else:
                back -= 1
            
            max_so_far = max(max_so_far, area)
        return max_so_far

            

           
        