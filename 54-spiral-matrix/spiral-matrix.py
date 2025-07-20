class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        top,left = 0,0
        right, bottom = len(matrix[0])-1,len(matrix)-1
        result = []
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            for j in range(top,bottom+1):
                result.append(matrix[j][right])
            right -= 1
            if top<= bottom:
                for k in range(right,left-1,-1):
                    result.append(matrix[bottom][k])
                bottom -= 1
            if left <= right:

                for l in range(bottom,top-1,-1):
                    result.append(matrix[l][left])
                left +=1
        return result
