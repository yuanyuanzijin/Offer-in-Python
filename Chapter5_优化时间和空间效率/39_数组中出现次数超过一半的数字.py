## 题目描述：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
## 超过数组长度的一半，因此输出2。如果不存在则输出0。

## 解法一，待更新，时间复杂度O(n)


## 解法二，时间复杂度为O(n)
class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = 0
        times = 0
        for n in numbers:
            if not times:
                tmp = n
                times = 1
            else:
                if n == tmp:
                    times += 1
                else:
                    times -= 1
        
        count = 0
        for n in numbers:
            if n == tmp:
                count += 1
        if count <= len(numbers) / 2:
            tmp = 0
        return tmp
