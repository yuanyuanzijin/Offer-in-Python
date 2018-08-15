## 题目描述：分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        tmp = []
        q = [root]
        restNum = 1
        nextNum = 0
        while q:
            if q[0].left:
                q.append(q[0].left)
                nextNum += 1
            if q[0].right:
                q.append(q[0].right)
                nextNum += 1
            tmp.append(q[0].val)
            q.pop(0)
            restNum -= 1
            if restNum == 0:
                result.append(tmp)
                tmp = []
                restNum = nextNum
                nextNum = 0
        return result
