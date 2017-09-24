# coding:utf-8

'''
date:2017/9/23
content:
克隆一张无向图，图中的每个节点包含一个 label 和一个列表 neighbors。
数据中如何表示一个无向图？http://www.lintcode.com/help/graph/
你的程序需要返回一个经过深度拷贝的新图。这个新图和原图具有同样的结构，并且对新图的任何改动不会对原图造成任何影响。
比如，序列化图 {0,1,2#1,2#2,2} 共有三个节点, 因此包含两个分隔符#。

第一个节点label为0，存在边从节点0链接到节点1和节点2
第二个节点label为1，存在边从节点1连接到节点2
第三个节点label为2，存在边从节点2连接到节点2(本身),从而形成自环。
我们能看到如下的图：

       1
    /  \ 
  /    \
 0 ---  2
      / \
     \_/
'''

import collections


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    '''solution 1'''

    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        #
        if node is None:
            return

        if node.label in self.dict:
            return self.dict[node.label]

        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root

        for nd in node.neighbors:
            root.neighbors.append(self.cloneGraph(nd))
        return root

    '''solution 2 '''

    def cloneGraph(self, node):
        # 前提判断
        if node is None:
            return

        # 通过BFS 获得graph中的所有节点
        nodes = self.getNodes(node)

        # 构造{原来节点：新构造节点}的hashmap，这个的核心作用是通过找原来节点的neighbors，找到其对应的新构建的节点
        mapping = {}
        for nd in nodes:
            mapping[nd] = UndirectedGraphNode(nd.label)

        # 通过nodes（图）中的每一个节点，将其邻居节点对应的新构造节点添加到当前节点的neighbors列表中
        for nd in nodes:
            new_node = mapping[nd]
            for neighbor in nd.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[node]

    def getNodes(self, node):
        # BFS for finding all the  nodes in graph
        queue = []
        results = set([node]) # 这里使用集合，就是为了避免图上的节点重复遍历
        queue.append(node)

        while queue:
            tmp = queue.pop(0)

            for neighbor in tmp.neighbors:
                if neighbor not in results:
                    results.add(neighbor)
                    queue.append(neighbor)
        return results


if __name__ == '__main__':
    pass
