# coding:utf-8

'''
date: 2017/11/19
content:
给出一个表达式 s，此表达式包括数字，以及字母方括号。
在方括号前的数字表示方括号内容的重复次数(括号内的内容可以是字符串或另一个表达式)，请将这个表达式展开成一个字符串。

样例
S = abc3[a] 返回 abcaaa
S = 3[abc] 返回 abcabcabc
S = 4[ac]dy 返回 acacacacdy
S = 3[2[ad]3[pf]]xyz 返回 adadpfpfpfadadpfpfpfadadpfpfpfxyz
'''


class Solution:
    """
    @param: s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        ''''''
        '''version 2: Recursive'''

        result = self.helper(s, 0, [])
        return result

    def helper(self, s, start, part):

        number = 0
        i = start
        while i < len(s):

            if s[i].isdigit():
                number = number * 10 + ord(s[i]) - ord('0')
                i += 1
            elif s[i] == '[':
                # concate the part and update the index
                newPart, j = self.helper(s, i+1, [])
                i = j + 1
                newPart *= number
                part.append(newPart)
                number = 0
            elif s[i] == ']':
                part = ''.join(part)
                return part, i
            else:
                part.append(s[i])
                i += 1
        return ''.join(part)


        '''version 1: Non-recursive Stack'''
    #     number = 0
    #     i = 0
    #     stack = []
    #
    #     while i < len(s):
    #         if s[i].isdigit():
    #             # if s[i] is a number
    #             number = number * 10 + ord(s[i]) - ord('0')
    #         elif s[i] == '[':
    #             stack.append(number)
    #             number = 0
    #         elif s[i] == ']':
    #             newString = self.popStack(stack)
    #             stack.append(newString)
    #         else:
    #             stack.append(s[i])
    #         i += 1
    #
    #     return ''.join(stack)
    #
    # def popStack(self, stack):
    #     reverse_stack = []
    #     part = ''
    #
    #     # take from stack
    #     while stack:
    #         tmp = stack.pop()
    #         if isinstance(tmp, int):
    #             # generate text
    #             while reverse_stack:
    #                 part += reverse_stack.pop()
    #             part *= tmp  # multiply the times
    #             break
    #         else:
    #             reverse_stack.append(tmp)
    #     return part

if __name__ == '__main__':
    string = "2[4[ab3[a]]5[6[abc66[a]]xy]uw]k"
    s = Solution()
    ret = s.expressionExpand(string)
    # ret = s.helper(string, 0, [])
    # ans = 'adadpfpfpfadadpfpfpfadadpfpfpfxyz'
    # assert ans == ret
    print(ret)



'''
1. 第一种方法：使用stack的非递归方法。
    （1）第一个点是：number的构造，这里的知识点主要是string to int的类型转换，以及遇到'32'怎么按每一位转换为32。
    （2）第二个点是：使用一个reverse_stack来接收stack中要弹出并拼接的元素，这样再使用reverse_stack弹出再拼接的
         方法能够保证字符的顺序不变，应该学习。
2. 第二种方法：使用递归，recursive
    （1）第一个点：遇到左括号[就往下递归，遇到有括号]就把已经拼接的part传回
    （2）第二个点：一定要注意每次要手动更新下标的位置，这是这个问题困扰我最大的地方。每次遇到]返回part的同时，还要
    把他的下标j一起返回，下一次接着走的时候就从i = j + 1继续走。
'''

