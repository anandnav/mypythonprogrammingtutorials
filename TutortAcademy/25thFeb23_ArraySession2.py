#189 Rotate Array
class Solution:
    def reverse(self,start,end,num: list[int]) -> list:
        while (start<end):
            num[start],num[end] = num[end],num[start]
            start += 1
            end-=1

    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        if (k >= l):
            k %= l
        self.reverse(0,l-k-1,nums)
        self.reverse(l-k,l-1,nums)
        self.reverse(0,l-1,nums)
        
    def trap(self, height: list[int]) -> int:       
        """
        start from right and put -1 if not not found highest value or put the highest value
        """ 
        maxfromleft = [0 for i in height]
        tempmax = 0
        for i in range(0,len(height)):
            tempmax = max(tempmax,height[i])
            if maxfromleft[i] < tempmax:
                maxfromleft[i] = tempmax
        maxfromright = [0 for i in height]
        tempmax = 0
        for i in range(len(height)-1,-1,-1):
            tempmax = max(tempmax,height[i])
            if maxfromright[i] < tempmax:
                maxfromright[i] = tempmax
        totaltraprain = 0
        for i in range(len(height)):
            
            totaltraprain += (min(maxfromleft[i],maxfromright[i])-height[i])
        return (totaltraprain)
        
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        countofi= 0
        res = 0
        hasodd = False
        for i in s:
            freq[i]= 1+freq.get(i,0)
        for k,v in freq.items():
            if v%2 == 0:
                res += v
            else:
                hasodd = True
        return hasodd + res        
        
mysol = Solution()
mysol.rotate(nums = [1,2,3,4,5,6,7], k = 3)
mysol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
mysol.longestPalindrome(s = "ccc")