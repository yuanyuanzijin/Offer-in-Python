## 题目描述：输入一个链表，输出该链表中倒数第k个结点。
## 定义两个指针
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p1 = head
        p2 = head
        c = 1
        if k <= 0:
            return None
        if not head:
            return None
        
        while head.next:
            head = head.next
            p1 = p1.next
            if c >= k:
                p2 = p2.next
            c += 1
        if c < k:
            return None
        return p2

        
## 自己的做法，会占用O(n)的空间
class Solution2:
    def FindKthToTail(self, head, k):
        # write code here
        array = []
        while head != None:
            array.append(head)
            head = head.next
        if k < 1 or len(array) < k:
            return None
        return array[-k]