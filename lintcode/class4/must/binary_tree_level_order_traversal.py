# coding:utf-8

'''
date:2017/9/21
content:
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
给一棵二叉树 {3,9,20,#,#,15,7} ：
  3
 / \
9  20
  /  \
 15   7
返回他的分层遍历结果：

[
  [3],
  [9,20],
  [15,7]
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
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        results = []
        if root is None:
            return results

        # create queue
        level = []
        level.append(root)
        while level:
            tmp_level = []
            length = len(level)
            for i in range(length):
                node = level.pop(0)
                tmp_level.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            results.append(tmp_level)
        return results


'''
总结：
1.BFS的核心结构就是队列，并且一定要记住是后入先出
2.容易在输出的时候搞混，但是要区分清楚谁是队列，谁是列表
'''
