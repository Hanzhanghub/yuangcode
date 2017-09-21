# coding:utf-8

'''
date: 2017/9/9
content: 
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
        :rtype: int
        """
        self.paths = 0
        self.helper(root,target)
        return self.paths

    def helper(self,root,target):
        '''最后的解法'''
        path = []
        if root is None:
            return

        left = self.helper(root.left,target)
        right = self.helper(root.right,target)


        path.append(root.val)
        if root.val == target:
            self.paths += 1


        if left is None and right is None:
            return path

        if left:
            for lp in left:
                lp += root.val
                if lp == target:
                    self.paths += 1
                path.append(lp)

        if right:
            for rp in right:
                rp += root.val
                if rp == target:
                    self.paths += 1
                path.append(rp)

        return path

if __name__ =='__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    s = Solution()
    ret = s.pathSum(tree,5)
    print ret

'''
1.第一次使用了返回路径列表的方法，但是超时了
第二次采用了返回一个列表，列表中是每条路的加权和
这样将遍历列表的复杂度降了下来，因此ac
2.
中途尝试了返回元祖的情况。返回元祖的情况在某些需要路径记忆的题中会有效果。
'''