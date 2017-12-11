# coding:utf-8

'''
date: 2017/11/22
content:
哈希表容量的大小在一开始是不确定的。
如果哈希表存储的元素太多（如超过容量的十分之一），我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。
假设你有如下一哈希表：
size=3, capacity=4
[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
哈希函数为：

int hashcode(int key, int capacity) {
    return key % capacity;
}
这里有三个数字9，14，21，其中21和9共享同一个位置因为它们有相同的哈希值1(21 % 4 = 9 % 4 = 1)。
我们将它们存储在同一个链表中。
重建哈希表，将容量扩大一倍，我们将会得到：
size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
给定一个哈希表，返回重哈希后的哈希表。

注意事项
哈希表中负整数的下标位置可以通过下列方式计算：
C++/Java：如果你直接计算-4 % 3，你会得到-1，你可以应用函数：a % b = (a % b + b) % b得到一个非负整数。
Python：你可以直接用-1 % 3，你可以自动得到2。
样例
给出 [null, 21->9->null, 14->null, null]
返回 [null, 9->null, null, null, null, 21->null, 14->null, null]
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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):

        # Calculate the size of hashTable
        size = len(hashTable)

        # Increase the size two times
        new_size = size * 2
        rehashedTable = [None] * new_size

        # Rehash
        for node in hashTable:
            # if node is None, move to the next position
            if node is None:
                continue

            # if node is a linked list
            while node.next is not None:
                # get current value, calculate the new hash key
                hash_code = self.hash_code(node.val, new_size)
                post = node.next
                node.next = None

                # add node to rehashedTable
                self.add_node(rehashedTable, hash_code, node)

                # turn to next node
                node = post

            # if node.next is None
            if node.next is None:
                hash_code = self.hash_code(node.val, new_size)
                self.add_node(rehashedTable, hash_code, node)

        return rehashedTable

    def hash_code(self, key, capacity):
        return key % capacity

    def add_node(self, hash_table,hash_code, node):
        if hash_table[hash_code] is not None:
            tmp = hash_table[hash_code]
            while tmp.next:
                tmp = tmp.next
            tmp.next = node
        else:
            hash_table[hash_code] = node

'''
1. 思路其实不难：先增加一倍size，然后循环原hash_table，遇到链表的节点，就循环这个链表直到下一个为空
2、要多考虑的一点是：当rehashedTable[i]已经有一个链表节点的时候，还要对他进行循环，然后把新的这个节点添加到链表
   的最后
'''








