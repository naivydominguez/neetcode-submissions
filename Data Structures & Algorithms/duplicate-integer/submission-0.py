class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}

        for elem in nums:
            if elem not in vals:
                vals[elem] = 1
            else:
                return True
        return False 
