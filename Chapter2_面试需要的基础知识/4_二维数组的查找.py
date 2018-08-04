## 比较矩阵的右上角和target，大则左移一列，小则下移一行
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        height = len(array)
        width = len(array[0])
        a = 0
        b = width-1
        while a <= height-1 and b >= 0:
            if array[a][b] == target:
                return True
            elif array[a][b] > target:
                b -= 1
            elif array[a][b] < target:
                a += 1
        return False