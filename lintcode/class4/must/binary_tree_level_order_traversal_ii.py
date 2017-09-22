# coding:utf-8

'''
date:2017/9/22
content:
给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）\
给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
按照从下往上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
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
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # 返回值
        results = []
        if root is None:
            return results

        # 队列
        queue = []
        queue.append(root)

        while queue:
            tmp = []
            queue_size = len(queue)

            for i in range(queue_size):
                node = queue.pop(0)
                tmp.append(node.val)

                # 层级遍历
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            results.append(tmp)
        results.sort(reverse=True)
        return results

'''
1.和1无本质区别，加了一个反序操作
'''