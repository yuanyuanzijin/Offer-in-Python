## 题目描述：在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
## 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
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
        