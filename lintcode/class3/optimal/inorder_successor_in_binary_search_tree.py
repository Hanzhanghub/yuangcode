# coding:utf-8
'''
Given a binary search tree (See Definition) and a node in it, 
find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.
'''
'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k


# function should return kth smallest element from the BST
'''解法一：还是使用divide和conquer的思路，把中序遍历都找出来，然后依次比对
缺点还是在于时间复杂度和空间复杂度上'''


def inorderSuccessor(root, X):
    # 完成中序遍历
    path = helper(root)
    if path is None:
        return -1
    else:
        # 由于是BST是严格的递增和递减
        for i in range(len(path)):
            if path[i] == X:
                return path[i + 1] if i < len(path) - 1 else -1
        return -1


def helper(root):
    if root is None:
        return

    left = helper(root.left)
    right = helper(root.right)

    if left is None and right is None:
        return [root]

    if left:
        if right:
            return left + [root] + right
        else:
            return left + [root]
    else:
        return [root] + right

'''解法二：先不断递归，找到这个p点，然后考虑以下三种情况
1.如果P没有右子节点，而且P是他父节点的左孩子，则要找的后继节点就是他的父节点
2. 如果P没有右子节点，而且P是他父节点的右孩子，则要找的后继节点就是他祖先节点里第一个是他父节点左子树的节点的父节点
3. 如果P有右子节点，则要找的后继节点就是以它右孩子为根的子树的最左面那个节点.'''
def solution2(root,p):
    ancestor = None
    while root is not None and root != p:
        if root.val > p.val:
            #　此时ｐ在root的左子树中
            #　并且只在这种情况下记录祖先，因为在中序遍历的时候，不能在右子树情况下记录祖先
            ancestor = root
            root = root.left
        else:
            root = root.right

    if root is None:
        return

    if root.right is None:
        return ancestor

    root = root.right
    if root.left is not None:
        root = root.left
    return root
