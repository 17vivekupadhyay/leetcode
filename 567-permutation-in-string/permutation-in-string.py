class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False   
        window = len(s1)
        def make_dict(string):
            compare = {}
            for i in range(window):
                if string[i] in compare:
                    compare[string[i]] += 1
                else:
                    compare[string[i]] = 1
            return compare

        s1dict = make_dict(s1)
        s2dict = make_dict(s2)

        for i in range(window, len(s2)):
            if s1dict == s2dict:
                return True

            if s2[i] in s2dict:
                s2dict[s2[i]] += 1
            else:
                s2dict[s2[i]] = 1

            s2dict[s2[i - window]] -= 1   

            if s2dict[s2[i - window]] == 0: 
                del[s2dict[s2[i - window]]]

        return s1dict == s2dict

        
            

        