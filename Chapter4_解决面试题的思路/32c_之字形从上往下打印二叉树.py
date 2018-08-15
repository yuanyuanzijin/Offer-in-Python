## 题目描述：之字形分行从上往下打印出二叉树的每个节点。
## 
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = [[root.val]]
        tmp = [root]
        tmp2 = []
        restNum = 1
        nextNum = 0
        order = True
        while tmp:
            node = tmp.pop(0)
            if order:
                if node.left:
                    tmp2.append(node.left)
                    nextNum += 1
                if node.right:
                    tmp2.append(node.right)
                    nextNum += 1
            else:
                if node.right:
                    tmp2.append(node.right)
                    nextNum += 1
                if node.left:
                    tmp2.append(node.left)
                    nextNum += 1
            restNum -= 1
            if restNum == 0:
                while tmp2:
                    tmp.append(tmp2.pop())
                if tmp:
                    result.append([i.val for i in tmp])
                restNum = nextNum
                nextNum = 0
                order = not order
        return result


## 在32b的问题上直接反转tmp
class Solution2:
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
        order = True
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
                if not order:
                    tmp.reverse()
                result.append(tmp)
                tmp = []
                restNum = nextNum
                nextNum = 0
                order = not order
        return result
