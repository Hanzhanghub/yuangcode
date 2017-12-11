# coding:utf-8

'''
date:2017/10/18
content:
设计实现一个带有下列属性的二叉查找树的迭代器：
元素按照递增的顺序被访问（比如中序遍历）
next()和hasNext()的询问操作要求均摊时间复杂度是O(1)
'''
"""
Definition of TreeNode:"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


"""Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.cur = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return self.cur is not None or len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        self.cur = self.stack.pop()
        next_value = self.cur.val
        self.cur = self.cur.right
        return next_value
