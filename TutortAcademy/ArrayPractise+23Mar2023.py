# 1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        #TC O(N^2)
        # maxnum = 0
        # res = []
        # for i in range(len(arr)):
        #     for j in range(i+1,len(arr)):
        #         if arr[j] > maxnum:
        #             maxnum = arr[j]
        #     res.append(maxnum)
        #     maxnum = 0
        # res[-1]=-1
        # return res
        
        #TC O(N)
        # maxonright = -1
        # for i in range(len(arr)-1,-1,-1):
        #     curr = arr[i]
        #     arr[i] = maxonright
        #     if curr > maxonright:
        #         maxonright = curr
        # return arr
        pass
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        #TC O(N)
        maxcandies = max(candies)
        res = []
        for i in candies:
            if i +extraCandies >= maxcandies:
               res.append(True)
            else:
                res.append(False)  
        return res
    
    def buildArray(self, nums: list[int]) -> list[int]:
        #TC O(N)
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        print(ans)

mysol = Solution()
mysol.replaceElements(arr = [17,18,5,4,6,1])
mysol.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1)
mysol.buildArray(nums = [0,2,1,5,3,4])