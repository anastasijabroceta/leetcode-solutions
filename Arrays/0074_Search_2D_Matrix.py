from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            arr=list(row)
            left=0
            right=len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        return False
if __name__=='__main__':
    so=Solution()
    matrix= [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target= 13
    print(so.searchMatrix(matrix,target))