# 　coding:utf-8

'''
date: 2017/9/9
content: 
给定一个二叉树，找出其最小深度。
二叉树的最小深度为根节点到最近叶子节点的距离。

给出一棵如下的二叉树:
        1

     /     \ 

   2       3

          /    \

        4      5  

这个二叉树的最小深度为 2
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
    @param root: The root of binary tree.
    @return: An integer
    """

    def minDepth(self, root):
        # paths = self.helper(root)
        # if paths:
        #     paths.sort(key=lambda x: len(x))
        #     return len(paths[0])
        # return 0  # else there is one node in tree
        min_len = self.helper(root)
        return min_len if min_len is not None else 0

    def helper(self, root):
        if root is None:
            return

        # path = []

        left = self.helper(root.left)
        right = self.helper(root.right)

        # 此时到达叶节点，开始计算深度
        if left is None and right is None:
            return 1
            # path.append([root.val])
            # return path

        if left:
            left += 1
            # for lp in left:
            #     lp.append(root.val)
            #     path.append(lp)
        if right:
            right += 1
            # for rp in right:
            #     rp.append(root.val)
            #     path.append(rp)

        if left is not None and right is not None:
            return min(right,left)
        elif left is None:
            return right
        elif right is None:
            return left
        else:
            return


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    s = Solution()
    ret = s.minDepth(tree)
    print(ret)


'''
1.第一次提交： 内存用完了
这种每一步都保存的方法确实垃圾
解决：
尝试有选择性的保存---未使用
使用了每次递归时返回当前的深度，加上一些简单判断即可
'''