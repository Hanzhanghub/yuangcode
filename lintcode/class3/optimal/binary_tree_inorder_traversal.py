# coding:utf-8

'''
date: 2017/9/9
content: 
给出一棵二叉树,返回其中序遍历
给出二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [1,3,2].
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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        path = []
        if not left:
            path.append(root.val)
        else:
            left.append(root.val)
            path += left

        right = self.inorderTraversal(root.right)
        if right:
            path.extend(right)
        return path


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    s = Solution()
    ret = s.inorderTraversal(tree)
    print(ret)
