class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = []
        for i in s:
            if i.isalnum():
                k.append(i.lower())
            
        k_str = ''.join(k)
        if len(k_str)==0:
            return True
        i=0
        j=len(k_str)-1
        while i<j:
            if k_str[i]!=k_str[j]:
                return False
            i+=1
            j-=1
        
        return True
                
            
           

        