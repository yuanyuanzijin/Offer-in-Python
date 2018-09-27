## 题目描述：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
## 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
## 改变原数组，时间O(n)，空间n
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) == 0 or len(numbers) == 1:
            return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                c = numbers[i]
                if numbers[c] == c:
                    duplication[0] = c
                    return True
                else:
                    numbers[i], numbers[c] = numbers[c], numbers[i]
            return False


## 不改变原数组，时间O(nlogn)(主要是排序用时)，空间n
class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) == 0 or len(numbers) == 1:
            return False
        numbers_new = sorted(numbers)
        old = None
        for n in numbers_new:
            if old and n == old:
                duplication[0] = n
                return True
            else:
                old = n
        return False

## 不改变原数组，时间O(nlogn)，空间1
## 待完成

