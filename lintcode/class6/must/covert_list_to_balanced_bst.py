# coding:utf-8

'''
date: 2017/11/5
content: 
给出一个所有元素以升序排序的单链表，将它转换成一棵高度平衡的二分查找树

样例
                2
1->2->3  =>   / \
             1  3
'''
"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        if head is None:
            return head

        ret = self.bstHelper(head)
        return ret

    def bstHelper(self, head, mid=None):
        if head == mid:
            return
        if head.next == mid:
            return TreeNode(head.val)

        # step 1: find the middle point
        fast, slow = head, head
        while fast.next != mid and fast.next.next != mid:
            fast = fast.next.next
            slow = slow.next

        # step 2: key point -- how to set the limit of each side
        root = TreeNode(slow.val)
        left_stop = slow
        right_stop = mid
        right_start = slow.next

        # step 3: construct the ROOT
        root.left = self.bstHelper(head, left_stop)
        root.right = self.bstHelper(right_start, right_stop)

        return root

if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    s = Solution()
    ret = s.sortedListToBST(node)
    print(ret.val)

'''
so fucking hard! lol!!
1.首先找到中间点mid,还是采用和sort_list中相同的思路：采用fast和slow的快慢指针
2.第二步是关键，要找到下一次递归的左区间端点和右区间的端点（我在这里浪费了许多时间）
3.第三步就是递归创建二叉平衡树
'''