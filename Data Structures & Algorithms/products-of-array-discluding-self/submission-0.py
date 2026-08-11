class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        pref = [1]*leng
        suff = [1]*leng
        res = [1]*leng

        for i in range(1,leng):
            pref[i] = pref[i-1]*nums[i-1]

        for j in range(leng-2,-1,-1):
            suff[j] = suff[j+1]*nums[j+1]
        

        for i in range(leng):
            res[i] = suff[i]*pref[i]

        
        return res



        