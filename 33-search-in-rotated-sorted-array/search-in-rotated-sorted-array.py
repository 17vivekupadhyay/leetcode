class Solution:
    def search(self, nums: List[int], target: int) -> int:

        front = 0
        back = len(nums) - 1


        while front <= back:
            mid = (front + back) // 2

            if nums[mid] == target:
                return mid

            if nums[front] <= nums[mid]:
                if nums[front] <= target < nums[mid]:
                    back = mid - 1
                else:
                    front = mid + 1
            else:
                if nums[back] >= target > nums[mid]:
                    front = mid + 1
                else:
                    back = mid - 1
            

        return -1

        