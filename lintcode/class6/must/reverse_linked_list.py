# coding:utf-8

'''
date: 2017/10/26
content: 
翻转一个链表

样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
'''
"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # special
        if head is None:
            return head

        dummy = ListNode(-1)
        tmp = dummy
        while head is not None:
            tmp1 = head.next
            head.next = tmp.next
            tmp.next = head
            head = tmp1
        return dummy.next

'''
1.这道题我也采用了:使用dummy节点，重新构建一个新的链表的思路。
2.只要注意好每次将head插入dummy的后边，然后移动head。
'''
