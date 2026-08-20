class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        back = len(nums)

        while front < back:
            mid = (front + back) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            
            if curr > target:
                back = mid
            else:
                front = mid + 1

        return -1
        