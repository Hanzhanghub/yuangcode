# coding:utf-8

'''
data: 2017/9/8
content: 
给定一个二叉树，判断它是否是合法的二叉查找树(BST)

一棵BST定义为：
节点的左子树中的值要严格小于该节点的值。
节点的右子树中的值要严格大于该节点的值。
左右子树也必须是二叉查找树。
一个节点的树也是二叉查找树。
      2
     / \
    1   4
       / \
      3   5
上述这棵二叉树序列化为 {2,1,4,#,#,3,5}.
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
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        self.flag = True
        self.helper(root)
        return self.flag


    def helper(self, root):
        if root is None:
            return

        # left=(left_max,left_min)
        # right=(right_max,right_min)
        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            return root.val, root.val

        l_max = -float('inf')
        l_min = float('inf')
        r_max = -float('inf')
        r_min = -float('inf')

        if left:
            if root.val <= left[0]:
                self.flag = False
                return None
            l_max = root.val
            l_min = left[1]
        if right:
            if root.val >= right[1]:
                self.flag = False
                return None
            r_max = right[0]
            r_min = root.val
        return max(l_max,l_min, r_max, r_min), min(l_max,l_min,r_max,r_min)

if __name__ == '__main__':
    # {10, 5, 15,  # ,#,6,20}
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    # tree.left.left = TreeNode(-4)
    # tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(20)

    s = Solution()
    ret = s.isValidBST(tree)
    print(ret)

