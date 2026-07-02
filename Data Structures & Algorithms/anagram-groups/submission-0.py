class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       result = defaultdict(list)


       for s in strs:
        count = [0] * 26 # a..z
        for c in s:
            
            #ord takes the ASCII value 
            count[ord(c) - ord('a')] += 1

            #lists cannot be dicts
        result[tuple(count)].append(s)
    
       return list(result.values())

