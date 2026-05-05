class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[m][-1]:
                l = m+1
            elif target < matrix[m][0]:
                r = m-1
            else :
                lin,rin = 0,len(matrix[m]) -1
                while lin <= rin:
                    m_in = (lin+rin)//2
                    if target > matrix[m][m_in]:
                        lin = m_in+1
                    elif target < matrix[m][m_in]:
                        rin = m_in-1
                    else:
                        return True
                return False
        return False