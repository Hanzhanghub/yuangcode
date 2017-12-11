# coding:utf-8

'''
date: 2017/10/17
content:
给出一棵二叉树,返回其中序遍历
'''

class Solution(object):
    def inorderTraversal(self,root):
        stack = []
        inorder = []

        # special circumstance
        if not root:
            return inorder

        cur = root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            tree_node = stack.pop()
            inorder.append(tree_node.val)
            cur = cur.right
        return inorder


