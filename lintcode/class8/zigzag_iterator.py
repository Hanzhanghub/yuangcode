# coding:utf-8


'''
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''
class zigzagIterator(object):
    def __init__(self, v1, v2):
        self.stack = []
        self.push_stack(v1, v2)

    def push_stack(self, a, b):
        tmp_stack = []

        # compare which list has a shorter length
        list_by_length = [None, None] # [0] for shorter, [1] for longer
        if len(a) > len(b):
            list_by_length[0] = b
            list_by_length[1] = a
        else:
            list_by_length[0] = a
            list_by_length[1] = b

        # zigzag read from a, b
        count = 0
        for i in range(len(list_by_length[0])):
            tmp_stack.append(list_by_length[0][i])
            tmp_stack.append(list_by_length[1][i])
            count = i
        tmp_stack += list_by_length[1][count + 1:]

        # reverse elements in tmp_stack into self.stack
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

    def hasNext(self,):
        return len(self.stack) != 0

    def next(self, ):
        if not self.hasNext():
            return None

        return self.stack.pop()


if __name__ == '__main__':
    v1 = [1, 2, 3, 4, 5, 6]
    v2 = [-1, -2, -3, -4, -5, -7]
    iter = zigzagIterator(v1, v2)
    result = []
    while iter.hasNext():
        result.append(iter.next())
    print(result)

'''
1. 仍然是和之前iterator同样的思路：先将zigzag序列构造好，然后通过两个stack来倒序这个zigzag序列
    （1）第一个点：构造zigzag。先选出两个序列哪个长度更短，这里我是用了一个列表来装比较了长度后的序列，
         以[0]表示长度短的，[1]表示长度长的。
    （2）第二：for循环长短短的序列，每次分别从两个序列中添加一个元素到tmp_stack中，这样就可以实现zigzag
'''

