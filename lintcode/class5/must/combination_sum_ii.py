# coding:utf-8

'''
date: 2017/10/11
content:
给出一组候选数字(C)和目标数字(T),找出C中所有的组合，使组合中数字的和为T。C中每个数字在每个组合中只能使用一次。

注意事项
所有的数字(包括目标数字)均为正整数。
元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
解集不能包含重复的组合。 

样例
给出一个例子，候选数字集合为[10,1,6,7,2,1,5] 和目标数字 8  ,
解集为：[[1,7],[1,2,5],[2,6],[1,1,6]]
'''

class Solution(object):
    def combination_sum_ii(self, num, target):
        results = []
        # special circumstance
        if not num:
            return results

        # sort
        num.sort()

        # DFS
        self.helper(start_index=0, partition=[], nums=num, remain_target=target, results=results)

        return results

    def helper(self,
               start_index,
               partition,
               nums,
               remain_target,
               results):

        # recursion entrance
        if remain_target == 0:
            results.append(list(partition))
            return

        # recursion disassemble
        for i in range(start_index, len(nums)):
            if nums[i] > remain_target:
                break

            if i != start_index and nums[i - 1] == nums[i]:
                continue

            partition.append(nums[i])
            self.helper(i + 1, partition, nums, remain_target - nums[i], results)
            partition.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [10, 1, 6, 7, 2, 1, 5]
    ret = s.combination_sum_ii(nums, 8)
    print(ret)
