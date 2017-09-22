# coding:utf-8

'''
date:2017/9/22
content:
给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行） 
给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
返回其锯齿形的层次遍历为：

[
  [3],
  [20,9],
  [15,7]
]
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
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # 返回值
        results = []
        if root is None:
            return results

        # 建立队列
        queue = []
        queue.append(root)

        # 之字形标志位
        zFlag = True

        while queue:
            tmp = []
            queue_size = len(queue)

            for i in range(queue_size):
                node = queue.pop(0)
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if zFlag:
                results.append(tmp)
            else:
                results.append(tmp[::-1])
            zFlag = not zFlag
        return results


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    s = Solution()
    ret = s.zigzagLevelOrder(tree)
    print(ret)

'''
1.以顺序的层序遍历为基础，根据要求，判断每一层的遍历结果是否需要反序
'''
