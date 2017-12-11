# coding:utf-8

'''
date: 2017/11/21
content:
Follow up Zigzag Iterator: What if you are given k 1d vectors? 
How well can your code be extended to such cases? 
The "Zigzag" order is not clearly defined and is ambiguous fork > 2 cases. 
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Example
Given k = 3 1d vectors:

[1,2,3]
[4,5,6,7]
[8,9]
Return [1,4,8,2,5,9,3,6,7].
'''
# import numpy as np
import random


class zigzagIterator(object):
    def __init__(self, k):
        self.stack = []
        # generate k 1d vectors
        kLists = []
        for i in range(k):
            kLists.append(list(range(i + 1, i + random.randrange(5, 10))))
        print(kLists)
        self.push_stack(kLists)

    def push_stack(self, arrays):

        tmp_stack = []

        # sort the arrays by their length
        arrays.sort(key=lambda x: len(x))

        # add the elements into tmp_stack
        i = 0
        while i < len(arrays[-1]):
            for j in range(len(arrays)):
                if i >= len(arrays[j]):
                    continue
                tmp_stack.append(arrays[j][i])
            i += 1

        # reverse the elements in tmp_stack into self.stack
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

        # print(self.stack)

    def hasNext(self, ):
        return len(self.stack) != 0

    def next(self, ):
        if not self.hasNext():
            return

        return self.stack.pop()


if __name__ == '__main__':
    iter = zigzagIterator(3)
    results = []
    while iter.hasNext():
        results.append(iter.next())
    print(results)

'''
1. 思路和zigzag_iterator一样，这里要注意的就是怎么考虑k个数组的之字形问题，我的想法是，先将所有的数组按照
   序列的长度排序，然后用一个双重循环，从长度小的序列开始，依次添加相应位置i的值。在这个过程中比较i和序列长度，
   如果i>=len(array[j]),那我们就跳过这个序列，去添加长度还够i的序列的值。
'''



