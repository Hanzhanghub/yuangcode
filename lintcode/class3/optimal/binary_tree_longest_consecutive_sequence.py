# coding:utf-8

'''
date:2017/9/10
content:
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
Especially, this path can be either increasing or decreasing. 
For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, 
the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
'''

'''
审题：
1.返回的是最长连续路径的长度，可以是顺序，也可以是倒序
2.最骚的是不限定在parent-child，可以是child-parent-child
'''


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def longest_consecutive_path(self, root):
        self.longest = 1
        self.helper(root)
        return self.longest

    def helper(self, root):
        path = []
        if root is None:
            return

        left = self.helper(root.left)
        right = self.helper(root.right)


        path.append([root.val])

        if left:
            for lp in left:
                lp.append(root.val)
                # 判断每一条路径里头有没有符合条件的
                if self.judge(lp):
                    path.append(lp)
                    if len(lp) > self.longest:
                        self.longest = len(lp)
            left = path

        if right:
            tmp = []
            for rp in right:
                rp.append(root.val)
                if self.judge(rp):
                    tmp.append(rp)
                    path.append(rp)
                    if len(rp) > self.longest:
                        self.longest = len(rp)
            right = tmp

        # 如果left和right的路径里都不为空，检查是否存在child-parent-child的情况
        if right and left:
            # 　注意right要取倒序，并且只取[1:]来合并（因为最后一个数是root.val）
            for lp in left:
                for rp in right:
                    one_path = lp + rp[::-1][1:]
                    if self.judge(one_path):
                        path.append(one_path)
                        if len(one_path) > self.longest:
                            self.longest = len(one_path)
        return path

    def judge(self,array):
        if len(array) >= 2 and abs(array[0] - array[1]) == 1 and sum(array) == ((array[0] + array[-1])*len(array)) / 2:
            return True
        else:
            return False

if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    # tree.left.left = TreeNode(4)
    # tree.left.right = TreeNode(5)

    s = Solution()
    ret = s.longest_consecutive_path(tree)
    print(ret)
