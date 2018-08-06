## 题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
## 本质上就是斐波那契数列
class Solution:
    def jumpFloor(self, number):
        # write code here
        ans = [0, 1, 2]
        for i in range(3, number+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[number]

class Solution2:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a, b = b, a + b
        return a

## 题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
## 本人思路：1到n-1个台阶，经不经过都行，所以每层两种可能，因此答案2的n-1次方
class SolutionC:
    def jumpFloorII(self, number):
        # write code here
        return 2 ** (number-1)