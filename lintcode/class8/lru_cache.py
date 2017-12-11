# coding:utf-8

'''
date:2017/11/22
content:
为最近最少使用（LRU）缓存策略设计一个数据结构，它应该支持以下操作：获取数据（get）和写入数据（set）。

获取数据get(key)：如果缓存中存在key，则获取其数据值（通常是正数），否则返回-1。

写入数据set(key, value)：如果key还没有在缓存中，则写入其数据值。
当缓存达到上限，它应该在写入新数据之前删除最近最少使用的数据用来腾出空闲位置。
'''

class LinkedList(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        """
        @param: key: An integer
        @return: An integer
        """
        self.stack = []
        self.capacity = capacity

    def get(self, key):
        # if key in stack, move the stack[key] to the first place
        hash_code = self.hash_code(key)
        if hash_code <= len(self.stack) - 1:
            tmp = self.stack.pop(hash_code)
            self.stack.insert(0, tmp)
            return self.stack[0]
        else:
            return -1

    def set(self, key, value):
        if len(self.stack) == self.capacity:
            # delete the last one in list

            # add the new one
            hash_code = self.hash_code(key)
            self.stack.pop(hash_code)
            self.stack.insert(0, value)


        else:
            # must consider there is a node in the position already


    def hash_code(self, key):
        return key % self.capacity





