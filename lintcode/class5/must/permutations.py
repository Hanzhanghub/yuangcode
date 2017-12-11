# coding:utf-8

'''
date: 2017./10/12
content:
给定一个数字列表，返回其所有可能的排列。

 注意事项
你可以假设没有重复数字。

样例
给出一个列表[1,2,3]，其全排列为：
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self,nums):
        results = []

        # special circumstance
        if not nums:
            return results

        # visited list
        visited = [0]*len(nums)

        # dfs
        self.helper(visited,nums,[],results)

        return results

    def helper(self,
               visited,
               nums,
               array,
               results):

        # recursion entrance
        if len(array) == len(nums):
            results.append(list(array))
            return


        # recursion disassemble
        for i in range(len(nums)):
            # examine whether i was visited
            if visited[i] == 1:
                continue

            # add action
            array.append(nums[i])
            visited[i] = 1

            # recursion
            self.helper(visited,nums,array,results)

            # remove action: back tracking
            array.pop()
            visited[i] = 0

if __name__ == '__main__':
    s = Solution()
    ret = s.permute([1,2,3])
    print(ret)


