class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        seen = {}
        longest = 1

        for fast in range(len(s)):
            if s[fast] not in seen:
                seen[s[fast]] = 1
            else:
                seen[s[fast]] +=1

            while (((fast - slow) + 1) - max(seen.values())) > k:
                seen[s[slow]] -= 1
                slow += 1

            longest = max(longest, (fast - slow) + 1)

        return longest
            
            





        