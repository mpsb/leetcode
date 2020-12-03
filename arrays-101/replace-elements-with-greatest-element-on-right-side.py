class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = len(arr) - 2
        largest = arr[-1]
        placeholder = 0

        while index >= 0:
            if arr[index] > largest:
                placeholder = largest
                largest = arr[index]
                arr[index] = placeholder
                print(placeholder, largest, arr[index])
            else:
                arr[index] = largest

            index -= 1

        arr[-1] = -1

        return arr