# coding:utf-8

'''
将一个二叉查找树按照中序遍历转换成双向链表。

给定一个二叉查找树：

    4
   / \
  2   5
 / \
1   3
返回 1<->2<->3<->4<->5。
'''

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""Definition of Doubly-ListNode"""
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        path = self.helper(root)
        if path is None:
            return
        else:
            list_node = DoublyListNode(path[0])
            node = list_node
            for i in range(1, len(path)):
                if i < len(path) - 1:
                    node.next = DoublyListNode(path[i])
                    node.prev = DoublyListNode(path[i])
                    node = node.next
                else:
                    if len(path) == 2:
                        node.next = DoublyListNode(path[i])
                    else:
                        node.next = DoublyListNode(path[i], DoublyListNode(path[i - 1]))

        return list_node

    def helper(self, root):
        if root is None:
            return

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            return [root.val]

        if left:
            if right:
                return left + [root.val] + right
            else:
                return left + [root.val]

        else:
            return [root.val] + right

'''
总结：
1、这道题注意一下双向链表的构建
'''
