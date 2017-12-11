# coding:utf-8

'''
date: 2017/11/13
content:
给一字串s和单词的字典dict,在字串中增加空格来构建一个句子，并且所有单词都来自字典。
返回所有有可能的句子。
 
样例
给一字串lintcode,字典为["de", "ding", "co", "code", "lint"]
则结果为["lint code", "lint co de"]。
'''


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        results = []
        # special condition
        if not s or s is None:
            return results

        # vocab collect
        vocabDict = self.vocab_collect(wordDict)
        '''11/15补充'''
        for letter in s:
            if letter in vocabDict:
                continue
            else:
                return results

        # dfs
        self.dfs_helper(1, [], s, wordDict, vocabDict, results)

        # return value
        return results

    def dfs_helper(self,
                   start_index,
                   partition,
                   s,
                   wordDict,
                   vocabDict,
                   results):

        # step 1: recursive exit
        if start_index == len(s) + 1:
            results.append(' '.join(partition))
            return

        # step 2: recursive disassemble
        for i in range(start_index, len(s) + 1):
            # add the space (cut), form a word
            tmp_word = s[:i]

            if len(tmp_word) == 1 and tmp_word not in vocabDict:
                break

            # examine whethe tmp_word in dictionary
            if self.is_word(tmp_word, wordDict):
                partition.append(tmp_word)
                tmp_s = s
                self.dfs_helper(1, partition, s[i:], wordDict, vocabDict, results)
                partition.pop()
                s = tmp_s

    def vocab_collect(self, word_dict):
        ret = set([])
        for word in word_dict:
            ret.update(set(word))
        return ret

    def is_word(self, word, dictionary):
        if word in dictionary:
            return True
        else:
            return False


if __name__ == '__main__':
    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # a = "lintcode"
    # dic = ["de", "ding", "co", "code", "lint"]
    s = Solution()
    ret = s.wordBreak(a, dic)
    print(ret)


'''
这道题的基础是常规的dfs，但是光是使用dfs做不出来，要添加：
1. dfs思路: 每次取一个词（从字母开始）， 如果他是一个字典里的词，就他这个词之后的字符串去重复判断
2. 添加vocabdict（构建成set类型，查找速度快）， 统计这个字典中出现的所有的字母。如果所给字符串中的字母不在这个vocabdict中，则直接返回空



'''