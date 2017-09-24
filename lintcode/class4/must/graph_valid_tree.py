# coding:utf-8

'''
date:2017/9/23
content:
给出 n 个节点，标号分别从 0 到 n - 1 并且给出一个 无向 边的列表 (给出每条边的两个顶点),
写一个函数去判断这张｀无向｀图是否是一棵树

给出n = 5 并且 edges = [[0, 1], [0, 2], [0, 3], [1, 4]], 返回 true.

给出n = 5 并且 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 返回 false.
'''

import collections
import queue
class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # 检查graph上的边是否满足构成树的基本要求
        if len(edges) != n-1:
            return False

        # 建立邻接字典，存储两点之间的联通情况
        neighbors = collections.defaultdict(list)
        for u,v in edges:
            neighbors[u].append(v) # 注意这里需要使用append，因为一点可能与多点相连
            neighbors[v].append(u)

        # 建立已遍历点的字典以及队列
        visits = {}
        queue = []
        queue.append(0)
        visits[0] = True

        # 依次根据连通节点遍历图中所有可能节点
        while queue:
            val = queue.pop(0)
            visits[val] = True

            for i in neighbors[val]:
                if not visits[i]:
                    visits[i] = True
                    queue.append(i)
        # 验证通过邻接边所遍历的所有节点是否等于图中的所有节点
        return len(visits) == n


'''
1.在图上进行BFS的思路与方法：
   （1）先要学会如何表示一张图。在本题中使用，neighbors表示图中邻接边的关系
   （2）进行BFS的时候，其实和树一样，检查通过邻接边能摸到的点，并记录和入栈
2.collections.defaultdict的使用：
    def __init__(self, default_factory=None, **kwargs)
    这个default_factory参数，我理解为使这个dict的keys具有default_factory的特性。
    例如在此题中使用list，那么在为keys增加value的时候，就可以将keys当作list来append(value)
'''
