# coding:utf-8

'''
date: 2017/10/10
content:
给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列

比如：
每次只能改变一个字母。
变换过程中的中间单词必须在字典中出现。

注意事项
如果没有转换序列则返回0。
所有单词具有相同的长度。
所有单词都只包含小写字母。

样例
给出数据如下：
start = "hit"

end = "cog"

dict = ["hot","dot","dog","lot","log"]

一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，

返回它的长度 5
'''

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # special
        if not dict:
            return 0

        # 这个我是不认同的，我认为应该和上面的特殊情况返回值相同
        if start == end:
            return 1

        # statics
        word_length = len(start)
        dict.append(end)
        mapping_dict = self.mapping(dict,word_length)

        # bfs
        result = 1
        visited = []
        visited_indx = range(word_length) # 解法二中记录已经匹配的下标位数
        queue = []
        queue.append(start)
        # queue.append((start,visited_indx)) # 解法二中的入队形式
        visited.append(start)

        '''解法二'''
        # 这个方法有误，错在每个字母并不是只能转化为目标词中的字母。这样做确实减少了复杂度，但是是因为考虑的情况少了
        # while queue:
            # size = len(queue)
            # result += 1
            # for i in range(size):
            #     pop_word = queue.pop(0)
            #     tmp_visited_indx = pop_word[1]
            #     for j in tmp_visited_indx:
            #         # change the word
            #         for k in mapping_dict[j]:
            #             if k != pop_word[0][j]:
            #                 tmp_word = pop_word[0][:j] + k + pop_word[0][j+1:]
            #                 # examine the word
            #                 if tmp_word == end:
            #                     return result
            #
            #                 # in dict judgement
            #                 if tmp_word in dict and tmp_word not in visited:
            #                     queue.append((tmp_word,tmp_visited_indx[:j]+tmp_visited_indx[j+1:]))
            #                     visited.append(tmp_word)


        '''解法一'''
        while queue:
            size = len(queue)
            result += 1
            for i in range(size):
                pop_word = queue.pop(0)
                for j in range(word_length):
                    # change the word
                    for k in mapping_dict[j]:
                        if k != pop_word[j]:
                            tmp_word = pop_word[:j] + k + pop_word[j + 1:]
                            # examine the word
                            # equal
                            if tmp_word == end:
                                return result
                            # in dict
                            if tmp_word in dict:
                                queue.append(tmp_word)
                                dict.remove(tmp_word) # TODO: 能AC的关键点：把每次遍历过的点删掉，那么在下一次找
                                                      # TODO: tmp_word是否在dict中的时候就减少了循环检查的次数

        return 0

    def mapping(self,dict,length):
        vocab = {}
        for i in range(length):
            vocab[i] = set([x[i] for x in dict])
        return vocab

if __name__ == '__main__':
    s = Solution()
    ret = s.ladderLength("hit","cog",["hot","dot","dog","lot","log"])
    # ret = s.ladderLength("a","c",["a","b","c"])
    print(ret)


'''
1.第一次尝试，方法正确。但超时了，在debug时我也发现会有许多重复的字母出现。
2.第二次尝试，方法错误。错在每个字母并不是只能转化为目标词中的字母
3.第三次尝试，终于正确。在第一次的基础上加入了两个改进：
    1.if k != pop_word[j]: 即相同的字母不在考虑
    2.dict.remove(tmp_word)，此为能AC的关键点：把每次遍历过的点删掉，那么在下一次找tmp_word
    是否在dict中的时候就减少了循环检查的次数
'''