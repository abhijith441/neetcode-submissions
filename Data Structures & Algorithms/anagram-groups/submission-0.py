class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hmap = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in hmap:
                hmap[sorted_str].append(string)
            else:
                hmap[sorted_str] = [string]
        
        for key, value in hmap.items():
            result.append(value)
        
        return result
            

        