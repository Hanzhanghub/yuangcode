# coding:utf-8

'''
date: 11/7
content:
Given an integer array, find a subarray with sum closest to zero. 
Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].
'''

import functools
class Node(object):
    def __init__(self, _val, _pos):
        self.value = _val
        self.pos = _pos

    #
    # def __cmp__(self, other):
    #     if self.value == other.value:
    #         return self.pos - other.pos
    #     return self.value - other.value

def cmp(x,y):
    if x.value == y.value:
        return x.pos - y.pos
    return x.value - y.value

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # special condition
        if not nums:
            return nums

        # TODO: step 1: prefixSum
        prefixSum = []
        prefixSum.append(Node(0, -1))
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            prefixSum.append(Node(sum, i))

        # TODO: step 2: sort the prefixSum, so that each node k in the sorted prefixSum, the node m
        # TODO: before the node k that has the closest value from the node.

        # watch out this point: in python 3.x, argument cmp is not used anymore
        # key = functools.cmp_to_key(lambda x,y: x.value - y.value) # first way to convert to key
        key = functools.cmp_to_key(cmp) # second way to convert to the key:also we can provide a function name
        prefixSum = sorted(prefixSum, key=key)

        result = [0, 0]
        closest_value = 100000000
        for j in range(len(prefixSum) - 1):
            if prefixSum[j + 1].value - prefixSum[j].value < closest_value or \
               (prefixSum[j + 1].value - prefixSum[j].value == closest_value and \
                min(prefixSum[j + 1].pos, prefixSum[j].pos) + 1 < result[0]):
                closest_value = prefixSum[j+1].value - prefixSum[j].value
                result[0] = min(prefixSum[j+1].pos, prefixSum[j].pos) + 1
                result[1] = max(prefixSum[j+1].pos, prefixSum[j].pos)
        return result


if __name__ == '__main__':
    a = [101, 33, 44, 55, 67, 78, -101, 33, -44, 55, -67, 78, -100, 200, -1000, 22, 100, 200, 1000, 22]
    s = Solution()
    ret = s.subarraySumClosest(a)
    print(ret)

'''
这道题值得好好地总结：
1.算法上：
    1.当普通的数据结构不够用时，应该学会自己创建数据结构。在这道题中，创建了自己的类Node，分别保留了点的值value和
    在原prefixSum中的位置。
    2.仍然是通过构建prefixSum来做，只是这是列表中存储的元素是Node节点，而不是单纯的数字。
    3.对prefixSum列表按照Node.value来排序，（排序时遇到了一个问题：python3.x的sort和sorted的自定义和python2.x的
    不同，这个在第二大点中在介绍。）
    4.构建了上述已排好序的列表后，思想就是，通过遍历一次列表中的节点，找到每个节点之前的节点（由于已经排好序，所以
    每个节点的之前的值一定是离他的值最近的一个），通过比较他们之间的差来找到最小的差，也即最接近与0的值。
2.实现方法上，也很值得学习：
    1.构建了自己的类，作为数据结构
    2.按照value进行排序sort。这里要注意，python 3.x中，sort和sorted中已没有cmp参数，所以原来可以通过雷属性__cmp__
    来排序的方式已经不能用了。改变为只能使用key参数，key参数的用法为：使用functools.cmp_to_key()来传入一个lambda
    或者是一个自己外部定义的函数。（通过代码review加深理解）
'''