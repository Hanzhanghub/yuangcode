# coding:utf-8

'''
date: 2017/11/23
content:
给定一个未排序的整数数组，找出最长连续序列的长度。

说明
要求你的算法复杂度为O(n)

样例
给出数组[100, 4, 200, 1, 3, 2]，这个最长的连续序列是 [1, 2, 3, 4]，返回所求长度 4
'''


class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        # special
        if not num:
            return 0

        # mapping
        mapDict = {}
        for x in num:
            mapDict[x] = 1

        longest = 0
        len_count = 0

        for x in num:
            if x in mapDict:
                del mapDict[x]
                len_count = 1
                l = x - 1  # only go to the left
                r = x + 1  # only go to the right

                while l in mapDict:
                    del mapDict[l]
                    len_count += 1
                    l = l - 1

                while r in mapDict:
                    del mapDict[r]
                    len_count += 1
                    r = r + 1
                if longest < len_count:
                    longest = len_count



        return longest







        # # mapping
        # mapDict = {}
        # visited = {}
        # for i in range(len(num)):
        #     mapDict[num[i]] = i
        #     visited[num[i]] = 0
        #
        # # loop for the next target
        #
        # count = 0
        # j = 0
        # start = 0
        # while j < len(num):
        #     next_suppose = num[start] + 1
        #     search_result = mapDict.get(next_suppose, -1)
        #     if search_result == -1:
        #         # indicate there is not a consecutive number
        #         start += 1
        #         visited[num[start]] = 1
        #     else:
        #         count += 1
        #         start = search_result
        #         if visited[num[start]] == 1:
        #             break
        #     j += 1
        #
        # return count


if __name__ == '__main__':
    a = [100, 4, 200, 1, 3, 2]
    s = Solution()
    ret = s.longestConsecutive(a)
    print(ret)


'''
1. 遍历一遍num，建立{num：1}的hash表
2. 循环num：
    （1）如果x在hash表中，考虑l = x -1; r = x + 1 
    （2）如果l在hash表中，则检查l = l - 1（一直往左）是否在hash表中
    （3）如果r在hash表中，则检查r = r + 1 （一直往右）是否在hash表中

'''