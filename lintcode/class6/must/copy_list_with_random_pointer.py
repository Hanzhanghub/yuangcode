# coding:utf-8

'''
date: 11/1
content:
给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。
返回一个深拷贝的链表。 
'''
"""
Definition for singly-linked list with a random pointer.
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        '''解法一：复习完copy graph 以后回来做这个题'''

        '''解法二：使用本节课视频的方法'''
        # special
        if head is None:
            return head

        # dummy construct
        dummy = RandomListNode(-1)
        dummy.next = head

        # step1: copy next
        self.copy_next(dummy)

        # step2: copy random
        self.copy_random(dummy)

        # step3: split list
        copy_list_dummy = self.split_list(dummy)

        # return
        return copy_list_dummy.next

    def copy_next(self, dummy):
        copy_next_head = dummy.next
        while copy_next_head:
            post = copy_next_head.next
            copy_node = RandomListNode(copy_next_head.label)
            copy_next_head.next = copy_node
            copy_node.next = post
            copy_next_head = post

    def copy_random(self, dummy):
        copy_random_head = dummy.next
        while copy_random_head:
            post = copy_random_head.next.next
            if copy_random_head.random is not None:
                copy_random_head.next.random = copy_random_head.random.next
            copy_random_head = post

    def split_list(self, dummy):
        split_head = dummy.next
        dummy2 = RandomListNode(-2)
        tmp = dummy2
        while split_head:
            tmp.next = split_head.next
            split_head.next = split_head.next.next
            tmp.next.next = None  # former error : split_head.next.next = None
            tmp = tmp.next
            split_head = split_head.next
        return dummy2

'''
分三步走：
1.copy next，使用同一个链表，在每个节点后添加拷贝节点
2.copy random，使用同一个链表，拷贝每个源节点的random，注意考虑random为None的情况
3.split list，将构造的整个节点分开。
'''

