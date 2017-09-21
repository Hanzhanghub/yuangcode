# coding:utf-8
'''
已知一颗二叉树，找到从根节点到任意节点的最大路径和
已知下面一颗二叉树

  1
 / \
2   3
返回4. (1->3)
'''

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):
    def path_sum(self,root):
        self.maximum = 0
        self.helper(root)
        return self.maximum

    def helper(self,root):
        if root is None:
            return

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            return root.val

        if left is not None:
            left = left + root.val
            if left  > self.maximum:
                self.maximum = left
        else:
            left = 0

        if right is not None:
            right = right + root.val
            if right > self.maximum:
                self.maximum = right
        else:
            right = 0
        return max(left,right,root.val)

        '''simple way'''
        if root is None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        return max(left,right) + root.val

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(-4)
    tree.right.left = TreeNode(-6)
    tree.right.right = TreeNode(-5)

    s = Solution()
    ret = s.path_sum(tree)
    print(ret)




