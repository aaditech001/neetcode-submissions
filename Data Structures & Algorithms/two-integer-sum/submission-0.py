class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # n=len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        has_map={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res in has_map:
                return [has_map[res],i]
            has_map[nums[i]]=i   