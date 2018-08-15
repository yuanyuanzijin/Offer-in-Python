## 题目描述：从上往下打印出二叉树的每个节点，同层节点从左至右打印。
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        q = [root]
        while q:
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            result.append(q[0].val)
            q.pop(0)
        return result
