# coding:utf-8


'''
date: 2017/12/7
content:
给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。

说明
最长上升子序列的定义：
最长上升子序列问题是在一个无序的给定序列中找到一个尽可能长的由低到高排列的子序列，这种子序列不一定是连续的或者唯一的。
https://en.wikipedia.org/wiki/Longest_increasing_subsequence

样例
给出 [5,4,1,2,3]，LIS 是 [1,2,3]，返回 3
给出 [4,2,4,5,3,7]，LIS 是 [2,4,5,7]，返回 4
'''

class Solution(object):
    def longest_increasing_subsequence(self, num):
        if not num:
            return 0

        # initial
        f = [1] * len(num)

        for i in range(1, len(num)):
            for j in range(i):
                f[i] = f[j] + 1 if num[j] < num[i] and f[j] + 1>= f[i] else f[i]

        return max(f)



if __name__ == '__main__':
    a = [3,4,5,6,2,43,53,43,1,13,4,45,2,3,4,65,5,3,6,5,4,7,8,6,9,4,9]
    s = Solution()
    ret = s.longest_increasing_subsequence(a)
    print(ret)


'''
1.这道题中要学习到动态规划方法的一般思路：
    （1）state：f[i]表示从任意一个木桩来，到我这个木桩的时候，最多才过多少木桩（并且这些木桩是从低到高排过序的）
    （2）function：f[i] = max{f[j] + 1}, 且j < i, num[j] < num[i]
    （3）initial：f = [1] * len(num)
    （4）answer：return max(f)
2.先要学会按照上面的思路去思考动态规划，必须有章法可循
'''











