# coding:utf-8

'''
date: 2017/10/25
content:
将两个排序链表合并为一个新的排序链表

样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
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
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        tmp = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is not None:
            tmp.next = l1
        if l2 is not None:
            tmp.next = l2
        return dummy.next


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(3)
    node.next.next = ListNode(8)
    node.next.next.next = ListNode(11)
    node.next.next.next.next = ListNode(15)
    node2 = ListNode(2)

    s = Solution()
    ret = s.mergeTwoLists(node, node2)
    while ret:
        print(ret.val)
        ret = ret.next

'''
这道题要注意一下思路：
我之前的想法一直都是判断哪个小，然后在两个链表中做插入。但这样带来的一个问题就是关系太复杂，容易把自己给搞蒙掉、
所以应该采用下面的思路：
1.建立dummy_node 
2.从dummy_node开始新建一个链表。即不断地，同时地对两个链表节点的值进行比较，谁小就先新建。最后剩下的那个链表直接
添加在新链表的结尾就可以了。
'''




