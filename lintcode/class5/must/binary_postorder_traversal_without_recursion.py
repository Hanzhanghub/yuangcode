# coding:utf-8
'''
date: 2017/10/17
content:
Given a binary tree, return the postorder traversal of its nodes' values. 

For example: 
Given binary tree {1,#,2,3},

1
  &nbsp;
   2 
  / 
 3 

return [3,2,1]. 
 Note: Recursive solution is trivial, could you do it iteratively?
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):
    def postorderTraversal(self,root):
        stack = []
        postorder = []
        visited = []

        if not root:
            return postorder

        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
                visited.append(node)
            else:
                postorder.append(node.val)
                node = None
        return postorder




if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left =  TreeNode(3)
    s = Solution()
    ret = s.postorderTraversal(root)
    print(ret)

'''
1.卡了一下，注意想清楚往右走的时候要将根节点进行入栈，并且已经遍历过的右子树要进行存储
'''