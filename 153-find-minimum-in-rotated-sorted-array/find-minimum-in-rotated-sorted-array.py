class Solution:
    def findMin(self, nums: List[int]) -> int:
        front = 0 
        back = len(nums) - 1
        while front < back:
            mid = (front + back) // 2
            if nums[mid] > nums[back]:
                front = mid + 1
            else:
                back = mid

        return nums[front]

        