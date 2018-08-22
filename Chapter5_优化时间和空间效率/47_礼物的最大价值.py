## 题目描述：在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定价值（大于0），从左上角开始，每次向下或向右走一格，直到棋盘的右下角，
## 请计算最多拿到多少价值的礼物？
## 牛客网没有该题
class Solution:
    def maxValue(self, array):
        self.array = array
        self.assist = [[0 for i in range(len(array[0]))] for j in range(len(array))]
        self.step(0, 0)
        return self.assist[-1][-1]


    def step(self, x, y):
        up = 0
        left = 0
        if x > 0:
            up = self.assist[x-1][y]
        if y > 0:
            left = self.assist[x][y-1]
        self.assist[x][y] = self.array[x][y] + max(up, left)
        print(self.assist)
        if x+1 < len(self.array):
            self.step(x+1, y)
        if y+1 < len(self.array[0]):
            self.step(x, y+1)

s = Solution()
array = [
    [1, 10, 3, 8],
    [12, 2, 9, 6],
    [5, 7, 4, 11],
    [3, 7, 16, 5]
]
print(s.maxValue(array))