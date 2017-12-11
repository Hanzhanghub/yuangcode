# coding:utf-8

'''
date:2017/11/20
content:
给你一个嵌套的列表，实现一个迭代器将其摊平。
一个列表的每个元素可能是整数或者一个列表。

注意事项
You don't need to implement the remove method.

给出列表 [[1,1],2,[1,1]]，经过迭代器之后返回 [1,1,2,1,1]。
给出列表 [1,[4,[6]]]，经过迭代器之后返回 [1,4,6]。
'''
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class NestedIterator(object):
    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = self.push_stack(nestedList)

    def push_stack(self, nestedList):
        tmp_stack = []

        for i in range(len(nestedList)):
            tmp_stack.append(nestedList[i])

        while tmp_stack:
            self.stack.append(tmp_stack.pop())

    def next(self):
        # @return {int} the next element in the iteration
        if not self.hasNext():
            return None

        return self.stack.pop().getInteger

    def hasNext(self):
        # @return {boolean} true if the iteration has more element or false
        while self.stack and not self.stack[-1].isInteger:
            self.push_stack(self.stack.pop())

        return len(self.stack) != 0



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

'''
1. 首先使用self.push_stack，将nestedList中的所有元素都以倒序的形式压入栈self.stack中----使用两个栈倒腾一次
2. self.next()基于self.has_next()完成，
    (1)如果self.has_next()返回False，那么self.next()返回None;
    (2)否则，返回self.stack.pop().getInteger() ==== 因为这时候self.stack的底部肯定是integer，即使是list也已被
       has_next()转换过了
3. self.has_next()检查栈底的元素是不是integer，如果不是，那么他是List，只需要将他传到self.push_stack中将List
   中元素取出，并且倒序加入self.stack中即可
'''






