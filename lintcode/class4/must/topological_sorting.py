# coding:utf-8

'''
date:2017/9/25
content:
给定一个有向图，图节点的拓扑排序被定义为：

对于每条有向边A--> B，则A必须排在B之前　　
拓扑排序的第一个节点可以是任何在图中没有其他节点指向它的节点　　
找到给定图的任一拓扑排序

例如，对于下列图：
这个图的拓扑排序可能是：
[0, 1, 2, 3, 4, 5]

或者

[0, 2, 3, 1, 5, 4]

或者
....
'''
# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 构造返回值
        results = []

        # 前提判断
        if graph is None:
            return []

        # 1. 统计各个节点的入度
        in_degree = self.helper_statistics(graph)

        # 2. 找到入度为0的节点，入队，进行BFS
        queue = []
        for node in graph:
            if in_degree[node] == 0:
                queue.append(node)
                results.append(node.label)

        while queue:
            nd = queue.pop(0)

            for neighbor in nd.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    results.append(neighbor.label)

        if len(results) == len(graph):
            return results
        return

    #　辅助函数，统计每个点的入度
    def helper_statistics(self,graph):
        in_degree = {}
        for node in graph:
            in_degree.setdefault(node,0)
            for neighbor in node.neighbors:
                in_degree.setdefault(neighbor,0)
                in_degree[neighbor] += 1
        return in_degree

'''
1.拓扑排序：循环删除入度为0的点，直到所有的点被遍历完
2.具体实现上：
    （1）先统计所有点的入度
    （2）入度为0的点入队列
    （3）减去一条入度边后检查其邻居，满足入度为0则入队列
    循环上述过程。
'''

