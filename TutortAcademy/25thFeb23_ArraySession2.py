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
       
        
mysol = Solution()
mysol.rotate(nums = [1,2,3,4,5,6,7], k = 3)