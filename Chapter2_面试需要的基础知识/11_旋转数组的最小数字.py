## 题目描述：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
## 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 给出的所有元素都大于0，若数组大小为0，请返回0。
## 如头小于尾，则未旋转；如头等于尾，则顺序查找；如头大于尾，则设置两个指针缩小范围，提高时间效率

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return None
        if len(rotateArray) == 1:
            return rotateArray[0]

        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        if rotateArray[0] == rotateArray[-1]:
            minValue = rotateArray[0]
            for i in range(len(rotateArray)):
                if rotateArray[i] < minValue:
                    minValue = rotateArray[i]
            return minValue
        
        p1 = 0
        p2 = len(rotateArray)-1
        while (p2 - p1) > 1:
            middle = (p1 + p2) // 2
            if rotateArray[middle] >= rotateArray[0]:
                p1 = middle
            else:
                p2 = middle
        return rotateArray[p2]
