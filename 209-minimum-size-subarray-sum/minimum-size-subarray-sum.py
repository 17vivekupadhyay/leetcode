class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        best = float('inf')
        slow = 0
        for fast in range(len(nums)):
            curr += nums[fast]
            
            while curr >= target:
                best = min(best, (fast - slow) + 1)
                curr -= nums[slow]
                slow += 1
            
        return 0 if best == float('inf') else best



        