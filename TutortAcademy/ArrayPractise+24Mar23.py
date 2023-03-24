#2433. Find The Original Array of Prefix Xor
# pref = [5,2,0,3,1] Output: [5,7,2,3,2]
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        minres = 0
        res =  []
        for i in range(0,len(pref)):
            res.append(minres^pref[i])
            minres = pref[i]  
        return res
        
mysol = Solution()
mysol.findArray(pref = [5,2,0,3,1])