class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero_count = 0

        for i in arr:
            if i == 0:
                zero_count += 1
                if zero_count == 2:
                    return True
                continue
            if i * 2 in arr:
                return True

        return False
