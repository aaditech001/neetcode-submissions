class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        sorted_value=sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        res=[]
        
        for i in range(k):
            res.append(sorted_value[i][0])
        return res
        