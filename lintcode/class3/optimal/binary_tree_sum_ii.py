# coding:utf-8

'''
date: 2017/9/9
content:
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = self.helper(root)
        ret_paths = []
        if paths is not None:
            for path in paths:
                if sum(path) == target:
                    ret_paths.append(path[::-1])
        return ret_paths

    def helper(self, root):
        path = []
        if root is None:
            return

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            path.append([root.val])
            return path

        if left is not None:
            for lp in left:
                lp.append(root.val)
                path.append(lp)

        if right is not None:
            for rp in right:
                rp.append(root.val)
                path.append(rp)
        return path


if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)


    s = Solution()
    ret = s.pathSum(tree,20)
    print(ret)

