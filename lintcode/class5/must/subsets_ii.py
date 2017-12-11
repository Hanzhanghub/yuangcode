# coding:utf-8

'''
date: 2017/11/13
content: 
给定一个可能具有重复数字的列表，返回其所有可能的子集

注意事项
子集中的每个元素都是非降序的
两个子集间的顺序是无关紧要的
解集中不能包含重复子集

样例
如果 S = [1,2,2]，一个可能的答案为：
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):

        results = []
        # special condition
        if not nums:
            return [results]

        # sort the array
        nums.sort()

        # recursive for dfs
        self.dfs_helper(0, [], nums, results)

        return results

    def dfs_helper(self,
                   start_index,
                   partition,
                   nums,
                   result):

        # step 1: recursive exit
        if partition not in result:
            result.append(list(partition))
            if len(partition) == len(nums):
                return

        # step 2: recursive disassemble
        for i in range(start_index, len(nums)):
            # avoid redudant
            if i != start_index and nums[i-1] == nums[i]:
                continue

            partition.append(nums[i])
            # step 3: recursive entrance
            self.dfs_helper(i+1, partition, nums, result)
            partition.pop()

if __name__ == '__main__':
    a = [1,2,2]
    s = Solution()
    ret = s.subsetsWithDup(a)
    print(ret)



