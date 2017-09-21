# coding:utf-8

'''
给出一棵二叉树，返回其节点值的前序遍历。
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
 返回 [1,2,3].
'''

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        path = self.helper(root)
        if path is None:
            return []
        else:
            return path

    def helper(self,root):
        if root is None:
            return

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            return [root.val]
        if left:
            if right:
                return [root.val] + left + right
            else:
                return [root.val] + left
        else:
            return [root.val] + right
