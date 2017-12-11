# coding:utf-8

'''
date: 2017/11/15
content:
 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 1 到 n，不是以 0 开头。

注意事项
你可以假设只有一组答案。

样例
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [1, 2].
'''

class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        results = []

        # special
        if not numbers:
            return results

        # Solution 1: hash map
        self.hashSolution(numbers, target, results)

        # Solution 2: two pointers
        # self.twoPointerSolution(numbers, target, results)
        # In this problem, There is no solution 2, as it requires to return the index of the number

        return results

    def hashSolution(self, numbers, target, results):
        # Construct a dict as hash map
        hash_map = {}
        for i in range(len(numbers)):
            hash_map[numbers[i]] = i

        # Cycle to find a and target - a
        for j in range(len(numbers)):
            remain = target - numbers[j]
            if remain in hash_map:
                if hash_map[remain] > j:
                    results.append(j+1)
                    results.append(hash_map[remain] + 1)
                else:
                    results.append(hash_map[remain] + 1)
                    results.append(j+1)
                break

        return results

if __name__ == '__main__':
    a = [2, 7, 11, 15]
    s = Solution()
    ret = s.twoSum(a, 9)
    print(ret)

'''
1.使用hashmap做，建立{nums[i]:i}的字典
2.找两数之和时，循环array中的每个元素a，并到hashmap中去找target-a是否存在
3.注：这道题还没法用two pointers来做，因为题目要求了下标不能变动
'''







