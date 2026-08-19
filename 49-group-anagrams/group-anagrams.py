class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            news = "".join(sorted(s))
            if news in seen:
                seen[news] += [s]
            else:
                seen[news] = [s]
        
        lst = []
        for keys in seen:
            lst.append(seen[keys])
        
        return lst


        