# coding:utf-8

'''
date: 2017/11/16
content:                                                          
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

注意事项
在三元组(a, b, c)，要求a <= b <= c。
结果不能包含重复的三元组。

样例
如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：
(-1, 0, 1)
(-1, -1, 2)
'''


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):

        results = []
        # special condition
        if not numbers:
            return results

        # Two pointers
        numbers.sort()

        for i in range(len(numbers)):
            target = - numbers[i]
            if i != 0 and numbers[i-1] == numbers[i]:
                continue
            self.twoSumSolution(numbers, target, i, results)

        return results

    def twoSumSolution(self, nums, target, c, results):
        if not nums:
            return
        head = c + 1 # 这是本题的关键，想清楚为什么每次从 c+1开始遍历 --- 这是因为你找的总target是0
        rear = len(nums) - 1

        while head < rear:

            if nums[head] + nums[rear] > target:
                rear -= 1
            elif nums[head] + nums[rear] < target:
                head += 1
            else:
                # reduce duplicate in DFS way
                if c < head:
                    results.append((-target, nums[head], nums[rear]))
                elif c > rear:
                    results.append((nums[head], nums[rear], -target))
                else:
                    results.append((nums[head], -target, nums[rear]))
                # avoid duplicates
                head += 1
                rear -= 1
                while head < rear and nums[head - 1] == nums[head]:
                    head += 1

                while head < rear and nums[rear + 1] == nums[rear]:
                    rear -= 1


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    ret = s.threeSum(nums)
    print(ret)

'''
1. 这道题的思想为：将3sum的问题化为2sum来做。具体的：
    1. 先把nums排好序，以能够用Two pointer的思想，实际上使用三指针，head，rear和i，
       每次固定一个i，得到-target[i]，然后求nums[i+1:]中的2sum为-target[i]的两个值
    2. 实现时要注意的地方有，
        （1）循环移动i指针的时候，如果nums[i] == nums[i-1],就可以跳过以避免重复
        （2）在每一次2sum的时候，注意避免重复的方法。
'''




