"""
归并排序（Merge Sort）
归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。 

算法描述
把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。
"""

def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    return merge(mergeSort(array[:mid]), mergeSort(array[mid:]))

def merge(left, right):
    p1 = 0
    p2 = 0
    newArray = []
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            newArray.append(left[p1])
            p1 += 1
        else:
            newArray.append(right[p2])
            p2 += 1
    if p1 < len(left):
        newArray += left[p1:]
    else:
        newArray += right[p2:]
    return newArray

a = [5, 4, 6, 5, 2, 3, 10, 9, 8, 6]
print(mergeSort(a))

