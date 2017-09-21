# coding:utf-8

'''
date: 2017/9/16
content: 将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。
http://www.lintcode.com/zh-cn/problem/flatten-binary-tree-to-linked-list/

note that: operate on original root !!
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
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """

    def flatten(self, root):
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return
        tmp = root

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left is None and right is None:
            return root

        if left is not None:
            root.right = left
            root.left = None
            # key poooooint !
            while tmp.right is not None:
                tmp = tmp.right


        if right is not None:
            # note that tmp and tree_node share the same reference
            tmp.right = right
            tmp.left = None
        return root


def preindx(root,ret):
    if root is None:
        return ret
    ret.append(root.val)
    preindx(root.left,ret)
    preindx(root.right,ret)
    return ret

def preindx2(root,ret):
    if root is None:
        return ret
    ret.append(root.val)
    preindx(root.right,ret)
    return ret

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right = TreeNode(3)
    node.right.right = TreeNode(6)

    print(preindx(node,[]))

    s = Solution()
    linklist = s.flatten(node)
    ret = preindx2(linklist,[])
    print(ret)