class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            i = 0
            try:
                while (i < len(arr)) and (arr[i] < arr[i+1]):
                    i += 1
            except IndexError:
                return False
                
            if (i == 0) or (i == len(arr)-1):
                return False
            
            while (i+1 < len(arr)) and (arr[i] > arr[i+1]):
                i += 1
            
            return i == len(arr)-1