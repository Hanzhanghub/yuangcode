# coding:utf-8

'''
date: 2017/11/21
content:
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]

By calling next repeatedly until hasNext returns false, 
the order of elements returned by next should be: [1,2,3,4,5,6].
'''

class twoDIterator(object):
    def __init__(self, vector):
        self.stack = []
        self.push_stack(vector)

    def push_stack(self, vector):
        tmp_stack = []

        # read number from 2d vector
        for i in range(len(vector)):
            tmp_stack += vector[i]

        # reverse elements from tmp_stack
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

    def hasNext(self, ):
        return len(self.stack) != 0

    def next(self, ):
        if not self.hasNext():
            return

        return self.stack.pop()


if __name__ =='__main__':
    vector = [[1,2],[3],[4,5,6]]
    iter = twoDIterator(vector)
    results = []
    while iter.hasNext():
        results.append(iter.next())
    print(results)

'''
1.思路和之前的iterator无二，多练习，唯手熟尔
'''



