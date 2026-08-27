class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []
        for string in strs:
            if "".join(sorted(string)) in anagrams:
                anagrams["".join(sorted(string))].append(string)
            else:
                anagrams["".join(sorted(string))] = [string]
        
        for key in anagrams:
            result.append(anagrams[key])
        
        return result

