# coding:utf-8

'''
date: 2017/10/10
content:
请找出无向图中相连要素的个数。
图中的每个节点包含其邻居的 1 个标签和 1 个列表。
（一个无向图的相连节点（或节点）是一个子图，其中任意两个顶点通过路径相连，且不与超级图中的其它顶点相连。）
给定图:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
返回 {A,B,D}, {C,E}。其中有 2 个相连的元素，即{A,B,D}, {C,E}
'''


class GraphNode(object):
    def __init__(self, label, neighbors):
        self.label = label
        self.neighbors = neighbors


class Solution(object):
    def connected_component_in_undirected_graph(self, nodes):
        # special circumstance
        if not nodes:
            return

        # 1. mapping
        mapping_dict = self.mapping(nodes)

        # 2. BFS
        result = []
        visited = []


        for node in mapping_dict.keys():

            if mapping_dict[node]:
                queue = []
                queue.append(node)
                tmp = []

                while queue:
                    # size = len(queue)
                    tmp_in = []
                    pop_node = queue.pop(0)
                    if pop_node not in visited:
                        tmp_in.append(pop_node.label)
                        for neighbor in mapping_dict[pop_node]:
                            if neighbor not in visited:
                                queue.append(neighbor)
                                tmp_in.append(neighbor.label)
                        visited.append(pop_node)
                        tmp += tmp_in
                        print(tmp)
                result.append(set(tmp))
        return result


    def mapping(self, nodes):

        mapping_dict = {}
        for node in nodes:
            mapping_dict.setdefault(node, [])
            for neighbor in node.neighbors:
                if neighbor in mapping_dict.keys():
                    continue
                mapping_dict[node].append(neighbor)
                mapping_dict.setdefault(neighbor,[])
        return mapping_dict

if __name__ == "__main__":
    graph1 = GraphNode(1,[])
    graph2 = GraphNode(2,[])
    graph3 = GraphNode(3,[])
    graph4 = GraphNode(4,[])
    graph5 = GraphNode(5,[])
    graph6 = GraphNode(6,[])
    graph1.neighbors = [graph2,graph3]
    graph2.neighbors = [graph1,graph3,graph6]
    graph3.neighbors = [graph1,graph2]
    graph4.neighbors = [graph5]
    graph5.neighbors = [graph4]

    s = Solution()
    ret = s.connected_component_in_undirected_graph([graph1,graph2,graph3,graph4,graph5])
    print(ret)
