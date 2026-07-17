class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        front = 0
        back = 0
        maxi = 0
        seen = {}
        tempk = 0
        size = 0

        while front <= back and back <= len(s) - 1:
            if s[back] in seen:
                seen[s[back]] += 1
                size += 1
                maxi = max(maxi, size)
            else:
                seen[s[back]] = 1
                tempk += 1

            back += 1
            if tempk > k:
                seen[s[front]] -= 1
                front += 1
                tempk = 0
                size = 0

        return maxi
        '''

        maxi = 0
        seen = {}
        front = 0
        for back in range(len(s)):
            if s[back] in seen:
                seen[s[back]] += 1
            else:
                seen[s[back]] = 1

            while ((back - front + 1)) - max(seen.values()) > k:
                seen[s[front]] -= 1 
                front += 1
            maxi = max(maxi, (back - front + 1))
        return maxi


