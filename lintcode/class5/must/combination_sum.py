# coding:utf-8

'''
date: 2017/10/11
content:
给出一组候选数字(C)和目标数字(T),找到C中所有的组合，使找出的数字和为T。C中的数字可以无限制重复被选取。

例如,给出候选数组[2,3,6,7]和目标数字7，所求的解为：
[7]，
[2,2,3]

注意事项
所有的数字(包括目标数字)均为正整数。
元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
解集不能包含重复的组合。 

样例
给出候选数组[2,3,6,7]和目标数字7
返回 [[7],[2,2,3]]
'''


class Solution(object):
    def combination_sum(self, candidates, target):

        results = []
        # special circumstance
        if not candidates:
            return [results]

        # array remove duplicate and sort
        no_duplicate_candidates = self.duplicate_remove(candidates)

        # DFS
        self.helper(start_index=0, partition=[], total_array=no_duplicate_candidates, remain_target=target,
                    results=results)

        # return value
        return results

    def helper(self,
               start_index,
               partition,
               total_array,
               remain_target,
               results):
        '''
        dfs manipulation 
        :param start_index: 
        :param partition: 
        :param total_array: 
        :param remain_target: 
        :param results: 
        :return: 
        '''

        # 递归的出口
        if remain_target == 0:
            results.append(list(partition))
            return

        # 递归的拆解
        for i in range(start_index, len(total_array)):
            if total_array[i] > remain_target:
                break
            #  因为这里的每个数是可以重复使用的，所以经过之前已经去重后，这里再一次检验，避免重复选择
            if i != start_index and total_array[i - 1] == total_array[i]:
                continue

            partition.append(total_array[i])
            self.helper(i, partition, total_array, remain_target - total_array[i], results)
            partition.pop()

    def duplicate_remove(self, nums):
        '''
        remove duplicate in nums and do the sorting action 
        :param nums: 
        :return: 
        '''
        nums.sort()
        i = 0
        j = i + 1
        while i < j and i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                nums = nums[:j] + nums[j + 1:]
            else:
                j += 1

            if j == len(nums) - 1:
                i += 1
                j = i + 1

        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,6,7]
    # rm_nums = s.duplicate_remove(nums)
    ret = s.combination_sum(nums,7)
    print(ret)

'''
1.首先是这道题需要进行排序，并且将数组去重
2.dfs的传统写法
3.值得注意的一点是这道题中数组的数字是可以重复选取的，所以我们递归的时候，应该从index开始，而不像之前的index+1开始
'''

