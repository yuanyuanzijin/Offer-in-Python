## 题目描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
## 设置两个指针，一个每次走两步，一个每次走一步，如果相遇则存在环。两个指针走过路径的差是环数量的倍数，2v-v=v，这个值和慢指针走过的路程相等。
## 将快指针放到起点，此时两个指针的路程差是环节点数的倍数。两个指针每次都走一步，当两个指针相遇时，相遇的位置即为入口节点。
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        pFast = pHead.next.next
        pSlow = pHead.next
        while pFast != pSlow:
            if pFast == None or pFast.next == None:
                return None
            pFast = pFast.next.next
            pSlow = pSlow.next
        
        pFast = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast


## 方法二，借助数组记录所有的节点，如果重复遇到，则为入口节点。空间消耗大。
class Solution2:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return None
        plist = []
        while pHead:
            if pHead not in plist:
                plist.append(pHead)
            else:
                return pHead
            pHead = pHead.next