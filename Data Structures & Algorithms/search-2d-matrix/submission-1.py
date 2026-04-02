class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r = 0, len(matrix[0]) - 1

        b,t = 0, len(matrix) - 1

        while b <= t:
            
            m1 = (b + t) // 2

            

            if matrix[m1][0] > target:
                t = m1 - 1
                
            elif matrix[m1][len(matrix[m1]) -1 ] < target:
                b = m1 + 1
            else:
                break
            
        while l <= r:
            m2 = (r + l) // 2
            
            if matrix[m1][m2] > target:
                r = m2 - 1
            elif matrix[m1][m2] < target:
                l = m2 + 1
            else:
                return True
    
        return False