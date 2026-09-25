class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasmap={}
        for i in range(len(nums)):
            hasmap[nums[i]]=hasmap.get(nums[i],0)+1
            if hasmap[nums[i]]>1:
                return True
        return False
        