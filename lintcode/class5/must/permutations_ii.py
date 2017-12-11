# coding:utf-8

'''
date: 2017/10/12
content:
给出一个具有重复数字的列表，找出列表所有不同的排列。

样例
给出列表 [1,2,2]，不同的排列有：
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
'''
class Solution(object):
    def permute_ii(self,nums):
        results = []

        # special circumstance
        if not nums:
            return [results]

        # visited documentary
        visited = [0] * len(nums)

        # sort the nums to prepare for the duplication removement
        nums.sort()

        # dfs
        self.helper(visited,nums,[],results)

        return  results

    def helper(self,
               visited,
               nums,
               permutation,
               results):

        # recursion entrance
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return

        # recursion disassemble
        for i in range(len(nums)):
            # duplictaed removement
            if (visited[i] == 1) or (i!=0 and nums[i-1] == nums[i] and visited[i-1]==0):
                continue

            #  add action: put forward
            permutation.append(nums[i])
            visited[i] = 1

            # recursion
            self.helper(visited,nums,permutation,results)

            # remove action: back tracing
            permutation.pop()
            visited[i] = 0

if __name__ == '__main__':
    s = Solution()
    ret = s.permute_ii([1,2,2])
    print(ret)


