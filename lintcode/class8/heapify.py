# coding:utf-8

'''
date: 2017/11/27
content:
给出一个整数数组，堆化操作就是把它变成一个最小堆数组。

对于堆数组A，A[0]是堆的根，并对于每个A[i]，A [i * 2 + 1]是A[i]的左儿子并且A[i * 2 + 2]是A[i]的右儿子。

说明
什么是堆？
堆是一种数据结构，它通常有三种方法：push， pop 和 top。
其中，“push”添加新的元素进入堆，“pop”删除堆中最小/最大元素，“top”返回堆中最小/最大元素。

什么是堆化？
把一个无序整数数组变成一个堆数组。如果是最小堆，每个元素A[i]，我们将得到A[i * 2 + 1] >= A[i]和A[i * 2 + 2] >= A[i]

如果有很多种堆化的结果？
返回其中任何一个。

样例
给出 [3,2,1,4,5]，返回[1,2,3,4,5] 或者任何一个合法的堆数组
'''
import heapq
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        ''''''
        '''Version 1: advanced data structure: PriorityQueue
        heapq.heapify(A)
        return A
        '''

        '''Version 2: siftdown'''
        for i in range(len(A)//2, -1, -1):
            self.siftdown(A, i)

        return A

    def siftdown(self, A, k):
        while k < len(A):
            smallest = k
            if k * 2 + 1 < len(A) and A[k*2+1] < A[smallest]:
                smallest = k * 2 + 1

            if k * 2 + 2 < len(A) and A[k*2+2] < A[smallest]:
                smallest = k * 2 + 2

            if smallest == k:
                break

            # exchange the value
            tmp = A[smallest]
            A[smallest] = A[k]
            A[k] = tmp

            # reset the pointer
            k = smallest


if __name__ == '__main__':

    a = [3,2,1,4,5]
    s = Solution()
    ret= s.heapify(a)
    print(ret)

'''
1，解法一：直接使用高级数据结构--PriorityQueue，其在Python中是heapq。可以直接使用heapq.heapify()
2. 解法二：从这个数组的中间位置开始，进行siftdown。我认为其原理在于：当下面的位置排好后，只需往上考虑，
   不用在考虑siftup。这个方法记下来，暂时理解的不是很深入。
'''




