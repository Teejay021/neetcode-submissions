class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #run a binary search on the first column then find the row and run binary search

        #for the first column
        #to be contained in a row must be 
        l = 0 
        r = len(matrix) -1
        row = 0
        while l <= r:
            mid = (l + r)//2
            if matrix[mid][0] == target:
                return True
            
            elif matrix[mid][0] < target and matrix[mid][len(matrix[0])-1] >= target:
                row = mid
                break
            elif matrix[mid][0] > target:
                r = mid -1
            elif matrix[mid][0] < target:
                l = mid + 1

        l = 0 
        r = len(matrix[row])-1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target: 
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1

        return False
