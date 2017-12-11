# coding:utf-8

'''
date: 2017/10/31
content:
Given a list, rotate the list to the right by k places, where k is non-negative.

Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
'''
"""
Definition for singly-linked list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: the List
    @param: k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):

        # special
        if head is None:
            return head

        #
        dummy1 = ListNode(-1)
        dummy1.next = head

        dummy2 = ListNode(-2)

        # count the length
        count_head = head
        count = self.length_count(count_head)
        k = k % count

        # find the position
        tmp = 1
        while tmp <= count - k:
            if tmp == count - k:
                post = head.next
                head.next = None
                head = post
                tmp += 1
                break
            head = head.next
            tmp += 1

        # rotate
        if tmp == 1:
            return dummy1.next

        tmp = dummy2
        while head:
            tmp.next = head
            tmp = tmp.next
            head = head.next

        tmp.next = dummy1.next
        return dummy2.next

    def length_count(self, head):
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count


if __name__ == '__main__':
    node = ListNode(1)
    # node.next = ListNode(2)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)
    # node.next.next.next.next = ListNode(5)

    # ret = node

    s = Solution()
    ret = s.rotateRight(node, 9)
    while ret is not None:
        print(ret.val)
        ret = ret.next

'''
这道题有三点需要注意：
1.首先是计算链表的长度。注意不要改变head的指向
2.注意判断何时不需旋转，直接返回原链表
3.注意k可以是大于链表长度的，这时候就需要利用取余的操作，将k变为量表长度的值
'''