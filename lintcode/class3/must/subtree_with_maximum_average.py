# coding:utf-8

'''
date: 2017/9/8
content: 
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Notice

LintCode will print the subtree which root is your return node. 
It’s guaranteed that there is only one subtree with maximum average.

Example 
Given a binary tree:

         1
      /   \  
    -5    11 
   / \   /  \ 
  1  2  4  -2 
return the node 11.
'''

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):
    def maximum_average(self,root):
        self.maximum = root
        self.helper(root)

        return self.maximum

    def helper(self,root):
        path = []
        if root is None:
            return

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            self.maximum = self.maximum if root.val < self.maximum.val else root
            path.append([root.val])
            return path

        if left:

            for p in left:
                p.append(root.val)
                maximum = sum([x for x in p]) / len(p)
                if maximum > self.maximum.val:
                    self.maximum = root
                path.append(p)

        if right:
            for p in right:
                p.append(root.val)
                maximum = sum([x for x in p]) / len(p)
                if maximum > self.maximum:
                    self.maximum  = root
                path.append(p)
        # print path
        return path

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(15)
    tree.right = TreeNode(11)
    tree.left.left = TreeNode(-4)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(-2)

    s =  Solution()
    ret = s.maximum_average(tree)
    print(ret.val)

