# coding:utf-8

'''
date: 2017/11/14
content:
给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

注意事项
小写字母或者大写字母他们之间不一定要保持在原始字符串中的相对位置。

样例
给出"abAcD"，一个可能的答案为"acbAD"
'''


class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        # special condition
        if not chars:
            return

        # two pointers
        lower = 0
        upper = 0

        while lower < len(chars) and upper < len(chars):
            while lower < len(chars) and not chars[lower].islower():
                lower += 1

            while upper < len(chars) and chars[upper].islower():
                upper += 1

            if lower < len(chars) and upper < len(chars):
                if lower > upper:
                    tmp = chars[lower]
                    chars[lower] = chars[upper]
                    chars[upper] = tmp
                else:
                    lower += 1
        return chars


if __name__ == '__main__':
    a = "abAcD"
    s = Solution()
    ret = s.sortLetters(a)
    print(ret)

'''
1.又是一道典型的两指针问题，解法类似于move_zeros 和 partition_array_by_odd_and_even
'''