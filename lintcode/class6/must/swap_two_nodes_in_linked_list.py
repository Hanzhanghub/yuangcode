# coding:utf-8

'''
date: 2017/10/30 
content:
Swap Two Nodes in Linked List 
Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. 
It's guaranteed there is no duplicate values in the linked list. 
If v1 or v2 does not exist in the given linked list, do nothing.

Notice 
You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.

Example 
Given 1->2->3->4->null and v1 = 2, v2 = 4.
Return 1->4->3->2->null.
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
    @param: v1: An integer
    @param: v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        if head is None or v1 == v2:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        # find two nodes
        v1_node, v2_node = self.find_prev(dummy, v1, v2)

        # swap two nodes
        if v2_node is None or v1_node is None:
            return dummy.next

        if v2_node.next == v1_node:
            self.swap_adjacent(v2_node)
        elif v1_node.next == v2_node:
            self.swap_adjacent(v1_node)
        else:
            self.swap_remote(v1_node, v2_node)

        return dummy.next

    def find_prev(self, dummy, v1, v2):
        head = dummy
        v1_node, v2_node = None, None
        while head.next:
            if head.next.val == v1:
                v1_node = head
            if head.next.val == v2:
                v2_node = head
            if v1_node is not None and v2_node is not None:
                break
            head = head.next
        return v1_node, v2_node

    # TODO: dummy->head->..->prev->node1->node2->post...
    # swap node1 & node2
    def swap_adjacent(self, prev):
        node1 = prev.next
        node2 = node1.next
        post = node2.next

        prev.next = node2
        node1.next = post
        node2.next = node1

    # TODO: dummy->head->..->prev1->node1->post1->...->prev2->node2->post2...
    # swap node1 & node2
    def swap_remote(self, prev1, prev2):
        node1 = prev1.next
        post1 = node1.next

        node2 = prev2.next
        post2 = node2.next

        prev1.next = node2
        node2.next = post1

        prev2.next = node1
        node1.next = post2


if __name__ == '__main__':
    node = ListNode(10)
    node.next = ListNode(8)
    node.next.next = ListNode(7)
    node.next.next.next = ListNode(6)
    node.next.next.next.next = ListNode(4)

    # ret = node

    s = Solution()
    ret = s.swapNodes(node, 8, 10)
    while ret is not None:
        print(ret.val)
        ret = ret.next

'''
1.将整段程序分为三个步骤完成：
    1.找到v1和v2两节点前的节点v1_node, v2_node
    2.判断两节点的相对位置：
        1.相邻：
            1.v1_node.next == v2_node，这里参照了答案的写法，先罗列出node1，node2，post，然后可以放心地调换
            2.v2_node.next == v1_node，同上
        2.非相邻：这是罗列出node1,post1,node2,post2，然后再放心调换
    3.返回dummy.next
'''
