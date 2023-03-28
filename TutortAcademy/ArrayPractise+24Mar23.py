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
        """
        TC = O(n^2)
        r = len(nums)//3
        res = []
        for i in nums:
            if (i not in res) and nums.count(i) > r:
                res.append(i) 
        return res 
        """
        # TC = O(n)
        # freq = {}
        # r = len(nums)//3
        # res = []
        # for i in nums:
        #     freq[i]= 1+freq.get(i,0)
        #     if freq[i] > r and (i not in res):
        #         res.append(i)
        # return res
        # Morrey's Voting Algorithm for TC O(n) and SC O(1)
        # num1,num2 = None,None
        # count1,count2=0,0
        # for num in nums:
        #     if num == num1:
        #         count1 +=1
        #     elif num == num2:
        #         count2 += 1
        #     elif count1 == 0:
        #         num1 = num
        #         count1 = 1
        #     elif count2 == 0:
        #         num2 = num
        #         count2 = 1
        #     else:
        #         count1 -=1
        #         count2 -= 1
        
        # count1,count2 = 0,0
        # for num in nums:
        #     if num == num1:
        #         count1 += 1
        #     elif num == num2:
        #         count2 += 1
        
        # n = len(nums)
        # res = []
        # if count1 > n//3:
        #     res.append(num1)
        # if count2 > n//3:
        #     res.append(num2)
        # return res
        pass
      
    def singleNumber(self, nums: list[int]) -> int:
        ones= 0
        twos= 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
        
mysol = Solution()
#mysol.findArray(pref = [5,2,0,3,1])
#print(mysol.majorityElement(nums = [2,2,1,1,5,6,5,5]))
print(mysol.singleNumber(nums = [0,1,0,1,0,1,99]))