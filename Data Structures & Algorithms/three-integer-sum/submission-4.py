class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skips duplicates in nums array
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums) - 1
            j = i+1
            target = -nums[i]

            while(j<k):
                if(nums[j]+nums[k] < target):
                    j +=1 
                elif nums[j]+nums[k] > target:
                    k -=1
                else:
                    res.append([nums[i],nums[j], nums[k]])
                    j += 1

                    # skips duplicates by comparing new val of j
                    # to the previous one that was just used 
                    while j < k and nums[j] == nums[j-1]:
                        j += 1 
                    

        return res
            


