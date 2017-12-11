# coding:utf-8

'''
date：2017/11/17
content：
找到两个数字使得他们和最接近target
样例
nums = [-1, 2, 1, -4],target = 4.
最接近值为 1
'''


class Solution(object):
    def two_sum_cloest(self, nums, target):
        '''
         nums: 
        target: 
        return: tuple(a,b) 
        '''
        result = [0] * 2

        # special condition
        if not nums:
            return ()

        # mapping: {value: index}
        mapping = self.mapping(nums)
        print(mapping)
        # sort nums
        nums.sort()

        left = 0
        right = len(nums) - 1
        nearest = max(nums)

        while left < right:
            if nums[left] + nums[right] < target:
                # compare the nearest one
                if abs(nums[left] + nums[right] - target) < nearest:
                    result[0] = mapping[nums[left]]
                    result[1] = mapping[nums[right]]
                    nearest = abs(nums[left] + nums[right] - target)
                left += 1
            elif nums[left] + nums[right] > target:
                # compare the nearest one
                if abs(nums[left] + nums[right] - target) < nearest:
                    result[0] = mapping[nums[left]]
                    result[1] = mapping[nums[right]]
                    nearest = abs(nums[left] + nums[right] - target)
                right -= 1
            else:
                result[0] = left
                result[1] = right
                break
        return result

    def mapping(self, nums):
        map_dict = {}
        for i in range(len(nums)):
            map_dict[nums[i]] = i
        return map_dict


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 4
    s = Solution()
    ret = s.two_sum_cloest(nums, target)
    print(ret)
