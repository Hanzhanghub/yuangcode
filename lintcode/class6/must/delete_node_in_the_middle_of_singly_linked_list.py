# coding:utf-8

'''
date: 2017/11/6
content: 
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。

样例
Linked list is 1->2->3->4, and given node 3, delete the node in place 1->2->4
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
    @param: node: the node in the list should be deleted
    @return: nothing
    """

    def deleteNode(self, node):
        # special condition
        if node is None:
            return

        # step 1: exchange the value of node and the value of node.next
        tmp_value = node.val
        node.val = node.next.val
        node.next.val = tmp_value

        # step 2: delete node.next
        post = node.next.next  # cuz node is either the first one and last one
        node.next.next = None
        node.next = post

'''
特征比较明显，由于只能是O(1)并且原地修改，所以：
1. 首先调换node和node.next的值
2. 然后把node.next删除即可

'''
