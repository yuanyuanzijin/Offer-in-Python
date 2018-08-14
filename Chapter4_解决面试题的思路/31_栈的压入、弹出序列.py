## 题目描述：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
## 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
## （注意：这两个序列的长度是相等的）
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        tmp = []
        p1 = 0
        p2 = 0
        length = len(pushV)
        
        for value in popV:
            while not tmp or tmp[-1] != value:
                if p1 < length:
                    tmp.append(pushV[p1])
                    p1 += 1
                else:
                    return False
            tmp.pop()
        return True


## 自己的方法
class Solution2:
    def IsPopOrder(self, pushV, popV):
        # write code here
        oldindex = 0
        for i in range(len(popV)):
            if popV[i] in pushV:
                index = pushV.index(popV[i])
            else:
                return False
            if i == 0 or oldindex <= index + 1:
                pushV.pop(index)
                oldindex = index
            else:
                return False
        return True
