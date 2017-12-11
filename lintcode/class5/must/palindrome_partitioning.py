# coding:utf-8

'''
date: 2017/10/11
content:
给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。
返回s所有可能的回文串分割方案。

样例
给出 s = "aab"，返回
[
  ["aa", "b"],
  ["a", "a", "b"]
]
'''


class Solution(object):
    def palindrome_partitioning(self, s):
        results = []
        # special circumstance
        if not s:
            return results

        # dfs
        self.helper(start_index=0, partition=[], string=s, results=results)

        return results

    def helper(self,
               start_index,
               partition,
               string,
               results):

        # recursion entrance
        if start_index == len(string):
            results.append(list(partition))
            return

        # recursion disassemble
        for i in range(start_index, len(string)+1):
            # 待判断文字
            tmp_s = string[start_index:i]
            if not tmp_s:
                continue
            if not self.isPalindrome(tmp_s):
                continue

            partition.append(tmp_s)
            self.helper(i, partition, string, results)
            partition.pop()

    def isPalindrome(self, s):
        # examine whether a word s is a palindrome
        if not s:
            return False

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    string = "aab"
    # print(s.isPalindrome(string))
    ret = s.palindrome_partitioning(string)
    print(ret)

'''
1.总结切割的方法，以及如何将其转化为dfs的一般题目
2.找到使用dfs的方法的题眼：不管其在原列表中的相对位置，并且要求求出所有的组合种数
'''