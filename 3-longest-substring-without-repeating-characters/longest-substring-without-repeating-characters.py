class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        front = 0
        back = 0
        size = 0
        largest = 0
        seen = set()

        while front <= back and back <= len(s) - 1:
            if s[back] not in seen:
                seen.add(s[back])
                back += 1
                size += 1
                if size >= largest:
                    largest = size
            else:
                seen.remove(s[front])
                size -= 1
                front += 1
            

        return max(size,largest)
        
        
        