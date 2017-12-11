# coding:utf-8

'''
date: 2017/11/28
content:
合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。

样例
给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null
'''
"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # step 1: traverse the lists
        # and store in a heap
        node_heap = []
        for i in range(len(lists)):
            # examine if it's a node
            tmp = lists[i]
            while tmp is not None:
                heapq.heappush(node_heap, tmp.val)
                tmp = tmp.next

        # step 2: reconstruct the linked list
        dummy = ListNode(-1)
        head = dummy

        while node_heap:
            pop_value = heapq.heappop(node_heap)
            head.next = ListNode(pop_value)
            head = head.next

        return dummy.next

'''
1. 将lists中的node中的值遍历出来，加入到最小堆中
2. 每次从最小堆中pop出最小的元素pop_value，强制最小堆重新找到下一个最小元素，将pop_value构建成新的node
'''







