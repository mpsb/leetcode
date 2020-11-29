class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i,e in enumerate(nums2):
                nums1[i] = nums2[i]
        else:
            nums1_index = 1

            for i in range(n):
                print(nums2[i],nums1[m-nums1_index], m-nums1_index)
                if nums2[i] >= nums1[m-nums1_index]:
                    nums1.insert(m-nums1_index+1,nums2[i])
                    nums1_index -= 1
                    del nums1[-1]
                    print(nums1)
                    continue
                else:
                    for j in range(m-nums1_index, -1, -1):
                        print(nums2[i], nums1[j], j)
                        if nums2[i] > nums1[j]:
                            nums1.insert(j+1, nums2[i])
                            nums1_index -= 1
                            del nums1[-1]
                            print(nums1)
                            break
                        elif j == 0:
                            nums1.insert(0, nums2[i])
                            nums1_index -= 1
                            del nums1[-1]
                            print(nums1)
                            break