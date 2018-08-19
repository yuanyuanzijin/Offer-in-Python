## 题目描述：请实现两个函数，分别用来序列化和反序列化二叉树
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.nodes = []
    
    def middleout(self, root):
        if root.left:
            self.middleout(root.left)
        self.nodes.append(str(root.val))
        if root.right:
            self.middleout(root.right)

    def __str__(self):
        self.nodes = []
        self.middleout(self)
        return " -> ".join(self.nodes)


class Solution:
    def __init__(self):
        self.p = 0

    def Serialize(self, root):
        # write code here
        if root == None:
            return '$,'

        s = str(root.val) + ','
        s += self.Serialize(root.left)
        s += self.Serialize(root.right)
        return s

    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        if s[-1] == ',':
            s = s[:-1]
        l = s.split(',')
        if self.p >= len(l):
            return None

        if l[self.p] != "$":
            root = TreeNode(int(l[self.p]))
            self.p += 1
            root.left = self.Deserialize(s)
            self.p += 1
            root.right = self.Deserialize(s)
            return root
        else:
            return None


## 测试用例
node = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))
s = Solution()
result = s.Serialize(node)
print(result)
tree = s.Deserialize(result)
print(s.Serialize(tree))
