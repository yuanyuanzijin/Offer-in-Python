## 题目描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
## 递归自己的写法
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        index = -1
        for i in range(len(sequence[:-1])):
            if sequence[i] > root:
                index = i
                break
        leftTree = sequence[:index]
        rightTree = sequence[index:-1]
        for r in rightTree:
            if r < root:
                return False
        result = True
        if leftTree:
            result = self.VerifySquenceOfBST(leftTree)
        if result and rightTree:
            result = self.VerifySquenceOfBST(rightTree)
        return result


## 递归子函数的写法
class Solution2:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.Verify(sequence)
    
    def Verify(self, sequence):
        if len(sequence) <= 1:          # <=2也是可以的
            return True
        root = sequence[-1]
        index = -1
        for i in range(len(sequence[:-1])):
            if sequence[i] > root:
                index = i
                break
        leftTree = sequence[:index]
        rightTree = sequence[index:-1]
        for r in rightTree:
            if r < root:
                return False
        return self.Verify(leftTree) and self.Verify(rightTree)
