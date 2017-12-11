# coding:utf-8

'''
date: 2017/10/31
content：
reorder list 
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln
reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Example
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.
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
    @param: head: The head of linked list.
    @return: nothing
    """

    def reorderList(self, head):

        # special
        if head is None:
            return head

        # reverse linked list and count the number
        tmp_head = head
        reverse_head, count = self.reverse(tmp_head)

        # recreate a linked list
        dummy = ListNode(-2)
        self.recreate(dummy, reverse_head, head, count)

        # return node
        return dummy.next

    def reverse(self, head):
        count = 0
        dummy = ListNode(-2)
        tmp = dummy
        while head is not None:
            post1 = head.next
            post2 = tmp.next
            tmp.next = ListNode(head.val)
            tmp.next.next = post2
            head = post1
            count += 1
        return dummy.next, count

    def recreate(self, dummy, rhead, head, count):
        tmp = dummy
        seq = 1
        while seq <= count:

            if seq % 2 != 0:
                # add from head
                post = head.next
                head.next = tmp.next
                tmp.next = head
                head = post
            else:
                # add from rhead
                rpost = rhead.next
                rhead.next = tmp.next
                tmp.next = rhead
                rhead = rpost
            seq += 1
            tmp = tmp.next


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    # node.next.next.next.next = ListNode(5)

    # ret = node

    s = Solution()
    ret = s.reorderList(node)
    while ret is not None:
        print(ret.val)
        ret = ret.next

'''
1.思路比较清晰，分为三步走：
    1.先把linked list翻转（reverse）。
        1.注意这里的翻转与之前的reverse_linked_list不同，在每次创建node时不再是对head的原地操作了，
        而是需要重新建立内存空间。否则，正向的head将会被消耗。
        2.同时记录这个链表的长度
    2.新建一个linked list，计数从1开始，单数就取正向的节点添加，双数就取反向的节点添加。
    3.返回dummy.next
    
'''