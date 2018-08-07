## 题目描述：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
## 每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
## 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
## 因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
## 和书上思路相似，不同的是使用了成员变量保存各个参数
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not path or rows == 0 or cols == 0:
            return False
        self.visited_index = []
        self.matrix = matrix
        self.path = path
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            for j in range(cols):
                if self.inPath(i, j):
                    return True
        return False

    def inPath(self, row, col):
        step = len(self.visited_index)
        if step == len(self.path):
            return True
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        index = self.cols * row + col    
        if index in self.visited_index:
            return False
        if self.matrix[index] == self.path[step]:
            self.visited_index.append(index)
            if self.inPath(row+1, col) or self.inPath(row-1, col) or self.inPath(row, col+1) or self.inPath(row, col-1):
                return True
            else:
                self.visited_index.pop()

## 测试用例
s = Solution()
print(s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))