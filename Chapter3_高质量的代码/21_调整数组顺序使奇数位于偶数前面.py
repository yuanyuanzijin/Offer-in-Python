## 题目描述：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
## 书上题目，不要求奇数的顺序不变，偶数顺序不变
class Solution:
    def isEven(self, value):
        return not (value & 1)

    def reOrderArray(self, array):
        # write code here
        if len(array) <= 1:
            return array
        p1 = 0
        p2 = len(array)-1
        while p1 <= p2:
            if self.isEven(array[p1]):
                p1 += 1
                continue
            if not self.isEven(array[p2]):
                p2 -= 1
                continue
            array[p1], array[p2] = array[p2], array[p1]
        return array


## 牛客网上题目，要求保证奇数和奇数，偶数和偶数之间的相对位置不变
class Solution:
    def reOrderArray(self, array):
        # write code here
        oddlist = []
        evenlist = []
        for i in array:
            if i & 1:
                oddlist.append(i)
            else:
                evenlist.append(i)
        return oddlist + evenlist
        