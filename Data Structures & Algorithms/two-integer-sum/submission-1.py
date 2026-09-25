class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap={}
        for i in range(len(nums)):
            gap=target-nums[i]
            if gap in hasmap:
                return [hasmap[gap],i]
            
            hasmap[nums[i]]=i
        