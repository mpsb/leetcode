class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        p1 = nums[-1]
        index = len(nums) - 2
        count = 1

        while index >= 0:
            if p1 != nums[index]:
                count += 1
                p1 = nums[index]
            else:
                nums.pop(index)
            index -= 1

        return count