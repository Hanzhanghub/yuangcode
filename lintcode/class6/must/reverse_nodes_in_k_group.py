# coding:utf-8

'''
date: 2017/10/25
content: 
给你一个链表以及一个k,将这个链表从头指针开始每k个翻转一下。
链表元素个数不是k的倍数，最后剩余的不用翻转。

样例
给出链表 1->2->3->4->5
k = 2, 返回 2->1->4->3->5
k = 3, 返回 3->2->1->4->5
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
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """

    def reverseKGroup(self, head, k):
        # special circumstance
        if not head:
            return

        # set dummy head
        dummy_head = ListNode(-1)
        dummy_head.next = head

        # count how many rounds
        counts = self.counts(head)
        # print(counts)

        # reverse the nodes
        head = dummy_head
        self.reverse(head, counts // k, k)

        # return value
        return dummy_head.next

    def counts(self, head):
        ret = 0
        while head:
            ret += 1
            head = head.next
        return ret

    def reverse(self, dummy, round, k):
        # reverse k
        for i in range(round):
            step = k
            head = dummy.next
            tmp = head.next
            while step > 1 and tmp:
                step -= 1
                head.next = tmp.next
                tmp.next = dummy.next
                dummy.next = tmp
                tmp = head.next
            dummy = head
        return


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    s = Solution()
    ret = s.reverseKGroup(node, 2)
    while ret:
        print(ret.val)
        ret = ret.next

'''
1.很久没做链表的题目，有点生疏。要找回怎么插入倒腾位置的感觉
2.在这道题中，我的一个想法就是：
    1.反正都要遍历一次链表，那我先遍历链表，找到有多少个元素，然后计算一下要翻转几个回合
    2.在每个回合中进行翻转
'''