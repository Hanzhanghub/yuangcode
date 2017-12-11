# coding:utf-8

'''
date: 2017/11/18
content:
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

注意事项
四元组(a, b, c, d)中，需要满足a <= b <= c <= d
答案中不可以包含重复的四元组。

样例
例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：

(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
'''


class Solution:
    """
    @param: numbers: Give an array
    @param: target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):

        '''版本二： 3sum 演进版'''
        results = []
        # special
        if not numbers:
            return results

        # 4sum to 3sum
        numbers.sort()
        for i in range(len(numbers)):
            remain_target = target - numbers[i]
            if i != 0 and numbers[i-1] == numbers[i]:
                continue
            self.threeSum(numbers, i+1, remain_target, results)

        return results


    def threeSum(self, nums, c, target, results):
        if not nums:
            return

        for j in range(c, len(nums)):
            remain_target = target - nums[j]
            if j != c and nums[j-1] == nums[j]:
                continue
            self.twoSum(nums, remain_target, j, c, results)

        return

    def twoSum(self, nums, target, c, b, results):
        if not nums:
            return

        head = c + 1  # 这是本题的关键，想清楚为什么每次从 c+1开始遍历 --- 这是因为你找的总target是0
        rear = len(nums) - 1

        while head < rear:

            if nums[head] + nums[rear] > target:
                rear -= 1
            elif nums[head] + nums[rear] < target:
                head += 1
            else:
                # reduce duplicate in DFS way
                if c < head:
                    results.append((nums[b-1], nums[c], nums[head], nums[rear]))
                elif c > rear:
                    results.append((nums[b-1],nums[head], nums[rear], nums[c]))
                else:
                    results.append((nums[b-1], nums[head], nums[c], nums[rear]))
                # avoid duplicates
                head += 1
                rear -= 1
                while head < rear and nums[head - 1] == nums[head]:
                    head += 1

                while head < rear and nums[rear + 1] == nums[rear]:
                    rear -= 1











        ''' 版本1： Time limit exceed'''
    #     results = set()
    #
    #     # special condition
    #     if not numbers:
    #         return results
    #
    #     # sort nums
    #     numbers.sort()
    #
    #     # construct a hash map
    #     hashmap = {}
    #     for a in range(len(numbers)):
    #         for b in range(a + 1, len(numbers)):
    #             hashmap.setdefault(numbers[a] + numbers[b], [])
    #             hashmap[numbers[a] + numbers[b]].append((a, b))
    #     print(hashmap)
    #
    #     # find target - c - d in hash map
    #     for c in range(len(numbers)):
    #         for d in range(c + 1, len(numbers)):
    #             # target - c - d in hash map
    #             if hashmap.get(target - numbers[c] - numbers[d]):
    #                 # calculate how many pairs in this hashmap[target - c -d]
    #                 for pair in hashmap[target - numbers[c] - numbers[d]]:
    #                     # examine whether a, b, c, d are all different
    #                     self.examine_difference(numbers, pair, c, d, results)
    #
    #     return list(results)
    #
    # def examine_difference(self, nums, pair, c, d, results):
    #     a, b = pair[0], pair[1]
    #     # c, d = c, d
    #
    #     # check sameness
    #     same_check = set([a, b, c, d])
    #     if len(same_check) != 4:
    #         return
    #
    #     # check dupplicates
    #     sort_index = tuple(sorted(([nums[a], nums[b], nums[c], nums[d]])))
    #     results.add(sort_index)
    #     return


if __name__ == '__main__':
    nums = [1,0,-1,-1,-1,-1,0,1,1,1,2]
    target = 2
    s = Solution()
    ret = s.fourSum(nums, target)
    print(ret)

'''
一波三折，直接用4sum变为3sum，3sum变为2sum的方法做，注意每个环节的衔接
'''


