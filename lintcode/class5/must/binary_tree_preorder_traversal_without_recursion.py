# coding:utf-8

'''
date: 2017/10/17
content:
Given a binary tree, return the preorder traversal of its nodes' values. 

For example: 
Given binary tree {1,#,2,3}, 
 1 
   \
    2 
  / 
 3 
return [1,2,3]. 
 ote: Recursive solution is trivial, could you do it iteratively?
'''
class Solution(object):
    def preorderTraversal(self,root):
        stack = []
        preorder = []
        # special circumstance
        if not root:
            return preorder

        # non recursion iterate
        stack.append(root)
        while not stack:
            tree_node = stack.pop()
            preorder.append(tree_node)
            if tree_node.right is not None:
                stack.append(tree_node.right)

            if tree_node.left is not None:
                stack.append(tree_node.left)

        return preorder






