class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i,e in enumerate(A):
            A[i] = e**2
            
        A.sort()
        
        return A
        