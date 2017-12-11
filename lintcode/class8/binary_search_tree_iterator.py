# coding:utf-8

'''
date: 2017/11/21
content:
设计实现一个带有下列属性的二叉查找树的迭代器：
元素按照递增的顺序被访问（比如中序遍历）
next()和hasNext()的询问操作要求均摊时间复杂度是O(1)

样例
对于下列二叉查找树，使用迭代器进行中序遍历的结果为 [1, 6, 10, 11, 12] 
   10
 /    \
1      11
 \       \
  6       12
'''
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
Example of iterate a tree:
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
        # do intialization if necessary
        self.stack = []
        self.push_stack(root)

    def push_stack(self, root):
        # read the binary search tree in inorder
        tmp_stack = self.inOrder(root)

        # put the elements read in tmp into self.stack in reverse order
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

    def inOrder(self, root):

        if root is None:
            return

        left = self.inOrder(root.left)
        right = self.inOrder(root.right)

        path = []
        if left is None and right is None:
            path.append(root)
            return path

        if left is not None:
            path += left
        path.append(root)
        if right is not None:
            path += right
        return path

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) != 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        if not self.hasNext():
             return None
        return self.stack.pop()


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(1)
    root.right = TreeNode(11)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(12)

    tree = BSTIterator(root)
    print(tree.hasNext())
    print(tree.next().val)
    ret = tree.inOrder(root)


'''
1.思路和flatten_nested_list_iterator一致
2.中序遍历
'''








