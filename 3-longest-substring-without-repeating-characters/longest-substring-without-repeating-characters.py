class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        slow = 0
        best = 0

        for fast in range(len(s)):

            while s[fast] in seen:
                seen.remove(s[slow])
                slow += 1

            seen.add(s[fast])
            best = max(best, (fast - slow + 1))
        return best

            
        