## 题目描述：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
## 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        self.result = []
        while rows > 2*start and columns > 2*start:
            self.printMatrixInCircle(matrix, rows, columns, start)
            start += 1
        return self.result

    def printMatrixInCircle(self, matrix, rows, columns, start):
        for i in range(start, columns-start, 1):
            self.result.append(matrix[start][i])
        for i in range(start+1, rows-start, 1):
            self.result.append(matrix[i][columns-start-1])
        if start < rows-start-1:
            for i in range(columns-start-2, start-1, -1):
                self.result.append(matrix[rows-start-1][i])
        if start < columns-start-1:
            for i in range(rows-start-2, start, -1):
                self.result.append(matrix[i][start])


## 之前自己的方法
class Solution2:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        new_list = []
        w = len(matrix[0])
        h = len(matrix)
        for c in range(min(w, h) + 1 // 2):
            for i in range(c, w-c, 1):
                if matrix[c][i] not in new_list:
                    new_list.append(matrix[c][i])
            for j in range(c+1, h-c-1, 1):
                if matrix[j][-1-c] not in new_list:
                    new_list.append(matrix[j][-1-c])
            for i in range(w-c-1, c-1, -1):
                if matrix[-1-c][i] not in new_list:
                    new_list.append(matrix[-1-c][i])
            for j in range(h-c-2, c, -1):
                if matrix[j][c] not in new_list:
                    new_list.append(matrix[j][c])
        return new_list