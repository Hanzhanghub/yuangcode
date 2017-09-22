# coding:utf-8

'''
date:2017/9/22
content:
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth D, you’ll have D linked lists).

Example 
Given binary tree:

      1
    / \ 
   2  3 
 / 
4 
return

[ 
1->null, 
2->3->null, 
4->null 
]
'''
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

class ListNode(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def convert_to_linked_list(self,root):
        #
        results = []
        if root is None:
            return results

        queue = []
        queue.append(root)

        while queue:
            tmp = []
            queue_size = len(queue)

            for i in range(queue_size):
                node = queue.pop(0)
                tmp.append(ListNode(node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            for j in range(len(tmp)):
                if j < len(tmp) -1:
                    tmp[j].next = tmp[j+1]
            results.append(tmp[0])
        return results

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    s = Solution()
    ret = s.convert_to_linked_list(tree)
    for i,node in enumerate(ret):
        print('{}th'.format(i))
        while node:
            print(node.val)
            node = node.next





