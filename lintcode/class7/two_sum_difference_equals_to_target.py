# coding:utf-8

'''
date: 2017/11/18
content:
Given an array of integers, find two numbers that their difference
equals to a target value.
where index1 must be less than index2. Please note that your returned 
answers (both index1 and index2) are NOT zero-based.

Notice：
It's guaranteed there is only one available solution

Example：
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
'''
class Solution(object):
    def difference_equals_target(self, nums, target):
        result = []

        # special condition
        if not nums:
            return result

        # hash map
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i

        # find target + j
        for j in range(len(nums)):
            if hashMap.get(target + nums[j]):
                a = hashMap[target+nums[j]]
                if a < j:
                    result.append(a+1)
                    result.append(j+1)
                else:
                    result.append(j+1)
                    result.append(a+1)
        return result


if __name__ == '__main__':
    nums = [2, 7, 15, 24]
    s = Solution()
    ret = s.difference_equals_target(nums, -9)
    print(ret)

'''
1.这道题我用传统的hashmap做
'''




