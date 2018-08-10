## 题目描述：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
import re

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        if s[0] in ['E', 'e']:
            return False
        if s[-1] in ['E', 'e']:
            return False
        
        tmp = re.split('e|E', s)
        if len(tmp) == 1:
            before_e = tmp[0]
            after_e = ""
        elif len(tmp) == 2:
            before_e = tmp[0]
            after_e = tmp[1]
        else:
            return False
        
        tmp = before_e.split('.')
        if len(tmp) == 2:
            zs = tmp[0]
            xs = tmp[1]
        elif len(tmp) == 1:
            if tmp[0][0] == '.':
                zs = ""
                xs = tmp[0][1:]
            elif tmp[0][-1] == ".":
                zs = tmp[0][:-1]
                xs = ""
            else:
                zs = tmp[0]
                xs = ""
        else:
            return False
        
        numlist = [str(k) for k in range(0, 10)]

        if zs:
            if zs[0] in ["+", '-']:
                zs = zs[1:]
            for i in zs:
                if i not in numlist:
                    return False
        
        for i in xs:
            if i not in numlist:
                return False
        
        if after_e:
            if after_e[0] in ["+", "-"]:
                after_e = after_e[1:]
            for i in after_e:
                if i not in numlist:
                    return False
        return True

## 正则表达式
class Solution2:
    # s字符串
    def isNumeric(self, s):
        # write code here
        return re.match('^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s)


s = Solution2()
test_list = ["+100","5e2","-123","3.1416","-1E-16","12e","1a3.14","1.2.3","+-5","12e+4.3"]
for t in test_list:
    print(s.isNumeric(t))