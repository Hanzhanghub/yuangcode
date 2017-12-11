# coding:utf-8

'''
date: 11/1
content:
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true
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
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        '''
        基本思路：使用快慢指针来做，若二者最后相交，则存在环；否则无环
        :param head: 
        :return: 
        '''
        # special 
        if head is None:
            return False

        # step1: construct dummy node, fast pointer, slow pointer 
        dummy = ListNode(-1)
        dummy.next = head

        fast_pointer = head  # two steps each time 
        slow_pointer = head.next  # one step each time
        
        # step2: loop for examine 
        while fast_pointer is slow_pointer:
            if fast_pointer.next is not None and fast_pointer.next.next is not None:
                fast_pointer = fast_pointer.next.next 
                slow_pointer = slow_pointer.next 
            else:
                return False 
        return True
    


        