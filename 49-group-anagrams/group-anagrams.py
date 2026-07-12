class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in seen:
                seen[x].append(strs[i])
            else:
                seen[x] = [strs[i]]
        
        builder = []
        for value in seen:
            builder.append(seen[value])
        
        return builder


        