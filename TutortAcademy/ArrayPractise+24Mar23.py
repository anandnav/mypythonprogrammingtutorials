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
    def majorityElement(self, nums: list[int]) -> int:
        # TC = O(n)
        # countofnums = {}
        # res,maxCount = 0,0
        # for i in nums:
        #     countofnums[i] =1+  countofnums.get(i,0)
        #     if countofnums[i] > maxCount:
        #       res = i 
        #     else:
        #       res
        #     maxCount = max(countofnums[i],maxCount)
        # return res 
        # TC O(N) Easy
        # count1 = 0
        # majorityele = 0
        # for i in nums:
        #     if count1 == 0:
        #         majorityele = i
        #     if majorityele == i:
        #         count1 += 1
        #     else:
        #         count1 -=1
        # print(majorityele)
        #Medium 229 Majority Element 2
        #Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

        
mysol = Solution()
#mysol.findArray(pref = [5,2,0,3,1])
mysol.majorityElement(nums = [3,3,4])