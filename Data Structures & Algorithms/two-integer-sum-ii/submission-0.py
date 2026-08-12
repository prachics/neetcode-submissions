class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0 
        j = len(numbers)-1
        res_sum=0

        while i<j:
            res_sum = numbers[i] + numbers[j]
            if res_sum == target:
                return [i+1,j+1]
            elif res_sum < target:
                i+=1
            else:
                j-=1
        
        