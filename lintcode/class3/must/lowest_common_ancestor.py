# coding:utf-8

'''
给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。
最近公共祖先是两个节点的公共的祖先节点且具有最大深度.
'''
"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


import copy


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        a = self.helper(root, A)
        b = self.helper(root, B)

        for i in a:
            if i in b:
                return i
        return

    def helper(self, root, target):
        path = []
        if root is None:
            return

        left = self.helper(root.left, target)
        right = self.helper(root.right, target)

        if root == target:
            path.append(root)
            return path

        if left:
            left.append(root)
            path = copy.copy(left)

        if right:
            right.append(root)
            path = copy.copy(right)
        return path


if __name__ == '__main__':
   tree = TreeNode(1)
   tree.left = TreeNode(2)
   tree.right = TreeNode(3)
   tree.left.left = TreeNode(4)
   tree.left.right = TreeNode(5)

   s = Solution()
   ret = s.lowestCommonAncestor(tree,tree.left.left,tree.right)
   print(ret.val)


'''
总结：
1.二叉树中的递归其深层原理都一样，就是以一种顺序往下遍历，但是由于题目不同，判断的具体写法不同
2.在这道题中，尤其要注意的是，左右子树返回不为空的写法：由于有可能是None，有可能是空列表[]， 所以应该写为if left/right:
'''