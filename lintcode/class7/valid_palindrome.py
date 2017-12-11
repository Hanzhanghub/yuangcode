# coding:utf-8

'''
date: 2017/11/9
content:
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。

注意事项
你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。
在这个题目中，我们将空字符串判定为有效回文。

样例
"A man, a plan, a canal: Panama" 是一个回文。
"race a car" 不是一个回文。
'''


class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # special
        if not s:
            return True

        # conver to lower type
        ref = "abcdefghijklmnopqrstuvwyz0123456789"
        s = s.lower()
        p1, p2 = 0, len(s) - 1
        while p1 <= p2:
            if s[p1] not in ref:
                p1 += 1
                continue
            if s[p2] not in ref:
                p2 -= 1
                continue

            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    string = "race e car"
    s = Solution()
    ret = s.isPalindrome(string)
    print(ret)

'''
1.nothing to say, it's really basic 
'''