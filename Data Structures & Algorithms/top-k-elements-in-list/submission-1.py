class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        l=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            l.append(sorted_freq[i][0])
        return l
