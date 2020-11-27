class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # weak solution. will improve on it.
        if 0 not in arr:
            return None

        o = len(arr)  # original size of array
        i = 0  # index

        while i < o - 1:
            if arr[i] == 0:
                for j in range(o - 2, i, -1):
                    arr[j + 1] = arr[j]
                arr[i + 1] = 0
                i += 2
            else:
                i += 1


