## 题目描述：牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，
## 但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
## Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
## Python方法
class Solution:
    def ReverseSentence(self, s):
        # write code here
        return ' '.join(reversed(s.split(' ')))


## 书中方法，先反转字符，后反转单词
class Solution2:
    def ReverseSentence(self, s):
        # write code here
        s = self.reversed(s)
        tmp = ''
        newstring = ''
        for i in s:
            if i == ' ':
                newstring += self.reversed(tmp) + ' '
                tmp = ''
            else:
                tmp += i
        if tmp:
            newstring += self.reversed(tmp)
        return newstring
        
    def reversed(self, s):
        new = ''
        for i in range(len(s)-1, -1, -1):
            new += s[i]
        return new

s = Solution2()
print(s.ReverseSentence("I am a student."))
