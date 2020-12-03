class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            index = 0

            for i in nums:
                if index == (len(nums)-1):
                    if i == nums[index-1]:
                        nums[index] = 'a'
                    break
                elif i != nums[index+1]:
                    if i == nums[index-1]:
                        nums[index] = 'a'
                elif i == nums[index+1]:
                    nums[index] = 'a'
                index += 1

            print(nums)
            while 'a' in nums:
                nums.remove('a')
        # nums = list(dict.fromkeys(nums))
        # print(nums)
        # return len(nums)