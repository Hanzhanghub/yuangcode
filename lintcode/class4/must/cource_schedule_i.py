# coding:utf-8

'''
date:2017/9/25
content:
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false
'''



class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # returen value
        if numCourses == 0 or not prerequisites:
            return True

        # 1.collection
        in_degree = self.helper(numCourses,prerequisites)

        # 2.BFS
        queue = []
        results = []
        for key in range(numCourses):
            if in_degree[key] == 0:
                queue.append(key)
                results.append(key)

        while queue:
            pop_num = queue.pop(0)
            for i in range(len(prerequisites)):
                if pop_num == prerequisites[i][1]:
                    l = prerequisites[i][0]
                    in_degree[l] -= 1
                    if in_degree[l] == 0:
                        queue.append(l)
                        results.append(l)
        # print(results)
        if len(results) == numCourses:
            return True
        else:
            return False

    def helper(self, num, pre):
        in_degree = {}

        for i in range(num):
            in_degree.setdefault(i,0)
        for j in pre:
            in_degree[j[0]] += 1
        # print(in_degree)
        return in_degree


if __name__ == '__main__':
    s = Solution()
    ret = s.canFinish(10, [[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]])
    print(ret)
