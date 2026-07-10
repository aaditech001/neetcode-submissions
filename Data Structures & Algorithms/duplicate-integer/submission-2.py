class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>1:
                return True
        return False   