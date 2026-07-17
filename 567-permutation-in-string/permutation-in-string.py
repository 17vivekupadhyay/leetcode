class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen1 = {}
        for i in range(len(s1)):
            if s1[i] not in seen1:
                seen1[s1[i]] = 1
            else:
                seen1[s1[i]] += 1

        seen2 = {}
        for i in range(len(s1)):
            if s2[i] not in seen2:
                seen2[s2[i]] = 1
            else:
                seen2[s2[i]] += 1


        front = 0
        back = len(s1)
        
        while back < len(s2):
            if seen1 == seen2:
                return True

            if s2[back] not in seen2:
                seen2[s2[back]] = 1
            else:
                seen2[s2[back]] += 1

            seen2[s2[front]] -= 1

            if seen2[s2[front]] == 0:
                del seen2[s2[front]]

            front += 1
            back += 1

        return seen1 == seen2

            


        

        
        



        