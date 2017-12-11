# coding:utf-8

'''
date:2017/9/24
content:
Given a undirected graph, a node and a target, 
return the nearest node to given node which value of it is target, return NULL if you can't find.
There is a mapping store the nodes' values in the given parameters.
Notice:
It's guaranteed there is only one available solution
'''

from queue import Queue
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        #
        if not graph or not values or node is None or not target:
            return

        if values[node] == target:
            return node

        queue = Queue()
        queue.put(node)
        visits = set([node])

        while queue:
            tmp_node = queue.get()
            for neighbor in tmp_node.neighbors:
                if values[neighbor] == target:
                    return node
                if neighbor not in visits:
                    visits.add(neighbor)
                    queue.put(neighbor)
        return

'''
1.弄清题意：给出图上一个点，找到图上值为target的离node最近的点
有一点要想清楚：第一次遇到的点一定是离node最近的点
2.常规的BFS流程
'''
