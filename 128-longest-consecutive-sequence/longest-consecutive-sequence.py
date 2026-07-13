class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force

        if nums == []:
            return 0
        nums = sorted(set(nums))
        print(nums)
        maxsofar = 1
        curr = 1
        for i in range(len(nums)-1):
            if nums[i + 1] == nums[i] + 1:
                curr += 1
            else:
                maxsofar = max(maxsofar,curr)
                curr = 1
        
        return max(maxsofar, curr)
        