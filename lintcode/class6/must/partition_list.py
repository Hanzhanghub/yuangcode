# coding:utf-8

'''
date: 2017/10/26
content: 
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。

样例
给定链表 1->4->3->2->5->2->null，并且 x=3

返回 1->2->2->4->3->5->null
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
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # special
        if not head:
            return head

        # dummy node
        dummy = ListNode(-1)
        dummy.next = head

        '''
        第一次尝试：超时
        find the node smaller than target x
        '''
        #     # set a flag inform that bigger in front of smaller
        #     head = dummy
        #     show_flag = False
        #     while head and head.next:
        #         if head.next.val < x :
        #             if show_flag:
        #                 # insert the proper location
        #                 self.sort_by_insert(dummy, head, head.next)
        #         else:
        #             show_flag = True
        #             head = head.next
        #
        #     # return value
        #     return dummy.next
        #
        # def sort_by_insert(self, head, former_node, the_node):
        #     while head and head.next:
        #         if head.next.val > the_node.val:
        #             # insert
        #             former_node.next = the_node.next
        #             the_node.next = head.next
        #             head.next = the_node
        #             return
        #         head = head.next

        '''second attendance'''
        head = dummy
        rear = head
        while rear and rear.next:
            if rear.next.val >= x:
                rear = rear.next
            else:
                if rear == head:
                    head = head.next
                    rear = head

                else:
                    # insert
                    tmp = rear.next.next
                    rear.next.next = head.next
                    head.next = rear.next
                    rear.next = tmp
                    head = head.next
        # return
        return dummy.next


if __name__ == '__main__':
    node = ListNode(-21)
    node.next = ListNode(-59)
    node.next.next = ListNode(4)
    node.next.next.next = ListNode(-99)
    node.next.next.next.next = ListNode(84)
    node.next.next.next.next.next = ListNode(-65)

    s = Solution()
    ret = s.partition(node, 54)
    while ret:
        print(ret.val)
        ret = ret.next

'''
1.第一次尝试----超时
2.第二次尝试——AC
    1.要先找到插入的位置---如果rear.next.val<x and rear == head，则说明下一个位置的点都小于x；
    2.要找到要插入的节点---如果rear.next.val<x and rear != head，这说明下一个位置的点就是要插入的节点
'''















