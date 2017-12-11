# coding:utf-8

'''
date: 2017/11/23
content:
给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。
如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。

注意事项
所有的字符串都只包含小写字母

样例
对于字符串数组 ["lint","intl","inlt","code"]
返回 ["lint","inlt","intl"]
'''

class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):

        results = []
        # special condition
        if not strs:
            return results

        # calculate the hash code
        hash_table = {}
        for word in strs:
            hash_code = ''.join(sorted(word))
            if hash_code not in hash_table:
                hash_table.setdefault(hash_code, [])
                hash_table[hash_code].append(word)
            else:
                hash_table[hash_code].append(word)

        for code in hash_table.keys():
            if len(hash_table[code]) > 1:
                results.append(hash_table[code])
        return results

if __name__ == '__main__':
    a= ["lint","intl","inlt","code"]
    s = Solution()
    ret = s.anagrams(a)
    print(ret)

'''
这道题的想法是：
1.遍历所给字符串数组strs中的每一个词，对着每一个词按字母的顺序进行排序：''.join(sorted(word))
  并以这个排好序后的word作为hash 的code。
2.对之后遍历的词，都以上述同样的方式，去检查是否已经存在于hash表中了，如果存在则进行保存。
'''

















