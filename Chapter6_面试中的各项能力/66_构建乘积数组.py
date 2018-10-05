## 题目描述：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = []
        C = [1]
        D = [1]
        for i in range(1, n):
            C.append(C[i-1]*A[i-1])
            D.insert(0, D[0]*A[n-i])
        for i in range(n):
            B.append(C[i]*D[i])
        return B
        

s = Solution()
print(s.multiply([1, 2, 3, 4, 5]))
