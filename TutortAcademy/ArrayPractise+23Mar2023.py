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
            
        

mysol = Solution()
print(mysol.replaceElements(arr = [17,18,5,4,6,1]))