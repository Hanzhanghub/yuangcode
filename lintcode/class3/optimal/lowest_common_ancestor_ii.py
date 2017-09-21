# coding:utf-8

'''
给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。
两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），离这两个节点最近的公共的节点。
每个节点除了左右儿子指针以外，还包含一个父亲指针parent，指向自己的父亲。
对于下面的这棵二叉树

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7

'''
"""
Definition of ParentTreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None

class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """

    '''解法一：还是使用divide和conquer的思路，把p，q的支路路径都找出来，然后依次比对
    缺点还是在于时间复杂度和空间复杂度上'''
    def lowestCommonAncestorII(self, root, p, q):
        # 找到p,q
        p_paths = []
        q_paths = []
        self.helper(root,p,p_paths)
        self.helper(root,q,q_paths)
        for i in p_paths:
            print(i.val)
        print('-----')
        for j in q_paths:
            print(j.val)
        print('-----')
        # 找公共祖先
        for node in p_paths:
            if node in q_paths:
                return node
        return None

    def helper(self,root,target,path):
            if root is None:
                return

            if root == target:
                path.append(root)
                return path

            left = self.helper(root.left,target,path)
            right = self.helper(root.right,target,path)

            if left:
                left.append(root)
                return left
            if right:
                right.append(root)
                return right
            return



if __name__ == '__main__':
    tree = TreeNode(4)
    tree.left = TreeNode(3)
    tree.right = TreeNode(7)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(6)

    s = Solution()
    ret = s.lowestCommonAncestorII(tree,tree.right.right,tree.right)
    print(ret.val)





