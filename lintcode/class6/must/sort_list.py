# coding:utf-8

'''
date: 2017/11/3
content:
Sort a linked list in O(n log n) time using constant space complexity.

Example
Given 1->3->2->null, sort it to 1->2->3->null.
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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):

        # special condition
        if head is None:
            return head
        if head.next is None:
            return head

        # # dummy
        # dummy = ListNode(-1)
        # dummy.next = head

        # step 1: find the middle point
        fast, slow = head, head
        mid = None

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        # step 2: recursive
        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        # merge sort
        sorted = self.merge(list1,list2)

        return sorted

    def merge(self,head,mid):
        if head == None:
            return mid
        if mid == None:
            return head

        # head is the left start, mid is the right start
        # exchange the nodes
        left_start = head
        right_start = mid
        dummy_merge = ListNode(-2)
        dummy_merge.next = head
        tmp = dummy_merge

        while left_start and right_start:
            if left_start.val >= right_start.val:
                # exchange two node
                post = right_start.next
                right_start.next = tmp.next
                tmp.next = right_start
                right_start = post
                tmp = tmp.next
            else:
                tmp = tmp.next
                left_start = left_start.next

        if left_start:
            tmp.next = left_start
        if right_start:
            tmp.next = right_start

        head = dummy_merge.next
        return head


if __name__ == '__main__':
    node = ListNode(5)
    node.next = ListNode(4)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    # node.next.next.next.next = ListNode(2)

    s = Solution()
    ret = s.sortList(node)
    while ret:
        print(ret.val)
        ret = ret.next


'''
本题思路：
1.怎么使用归并？===>使用快慢指针fast, slow。当fast.next 或者 fast.next.next中有一个为None时，
中间点即为mid = slow.next
2.何时开始merge左右链表？===>当head.next is None 且 mid is None的时候，开始合并
3.怎么排序然后归并？===>使用head的这半个链表，当mid区的值小的时候，将mid区的node插入到head这个链表中。
'''




