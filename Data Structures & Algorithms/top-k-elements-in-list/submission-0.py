class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        l = []

        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        
        sorted_values = sorted(freq.items(),key = lambda x:x[1],reverse=True) 

        for i in range(k):
            l.append(sorted_values[i][0])
        

        return l


        