# coding:utf-8

'''
date: 2017/10/26
content: 
翻转链表中第m个节点到第n个节点的部分
注意事项
m，n满足1 ≤ m ≤ n ≤ 链表长度

样例
给出链表1->2->3->4->5->null， m = 2 和n = 4，返回1->4->3->2->5->null
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
    @param: head: ListNode head is the head of the linked list 
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # 这道题按我的做法话，特殊情况要多考虑一下
        if head is None or head.next is None or m == n:
            return head

        dummy = ListNode(-1)
        tmp = dummy
        point_m = None
        count = 1

        while head:
            if count < m:
                tmp1 = head.next
                tmp.next = head
                head = tmp1
                tmp.next.next = None
                tmp = tmp.next
            if count == m:
                tmp1 = head.next
                tmp.next = head
                head = tmp1
                tmp.next.next = None
                point_m = tmp.next
            if m < count < n:
                tmp1 = head.next
                head.next = tmp.next
                tmp.next = head
                head = tmp1
            if count == n:
                tmp1 = head.next
                head.next = tmp.next
                tmp.next = head
                head = tmp1

                tmp = point_m
                break

            count += 1

        if head is not None:
            tmp.next = head

        return dummy.next


if __name__ == '__main__':
    node = ListNode(3760)
    # tmp = node
    # nums = [3760, 2881, 7595, 3904, 5069, 4421, 8560, 8879, 8488, 5040, 5792, 56, 1007, 2270, 3403, 6062]
    # for i in range(1, len(nums)):
    #     tmp.next = ListNode(nums[i])

    node.next = ListNode(2)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)
    # node.next.next.next.next = ListNode(5)
    # node.next.next.next.next.next = ListNode(6)
    # node.next.next.next.next.next.next = ListNode(7)

    s = Solution()
    ret = s.reverseBetween(node, 1,2)
    while ret:
        print(ret.val)
        ret = ret.next

'''
1.这道题我的逻辑：
    1.从dummy开始创建新的链表
    2.关键点为记录m对应的节点，这个节点对应于最后倒序完成后的最后一个位置
    3.将上述最后一个位置与head已经走到的位置相结合，则完成
这样做的话，就是要考虑的特殊情况更多。
'''