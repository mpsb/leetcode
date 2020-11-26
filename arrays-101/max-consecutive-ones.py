class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        else:
            
            a = 0
            m = 0
        
            for i in nums:
                if i == 1:
                    a+=1
                    if a > m:
                        m = a
        
                else:
                    a = 0 
        
        return m