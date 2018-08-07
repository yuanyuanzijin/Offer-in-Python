## 题目描述：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
## 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
## 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows <= 0 or cols <= 0 or threshold < 0:
            return 0
        self.threshold = threshold
        self.rows = rows
        self.cols =cols
        self.visited_index = []
        self.allow(0, 0)
        return len(self.visited_index)
    
    def allow(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.cal(row, col) > self.threshold:
            return
        index = self.cols * row + col    
        if index in self.visited_index:
            return
        self.visited_index.append(index)
        if not (self.allow(row+1, col) or self.allow(row-1, col) or self.allow(row, col+1) or self.allow(row, col-1)):
            return

    def cal(self, row, col):
        valsum = 0
        for d in str(row)+str(col):
            valsum += int(d)
        return valsum

## 测试用例
s = Solution()
print(s.movingCount(18, 30, 30))