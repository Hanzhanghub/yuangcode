# coding:utf-8

'''   
date: 2017/11/14
content: 
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。
我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

注意事项
不能使用代码库中的排序函数来解决这个问题。
排序需要在原数组中进行。

样例
给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。
'''


class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # special
        if not nums:
            return

        # two pointers (actually three pointers)
        i = 0
        left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                # exchange with left pointer
                if left < i:
                    tmp = nums[i]
                    nums[i] = nums[left]
                    nums[left] = tmp
                    left += 1
                else:
                    i += 1

                # tmp = nums[i]
                # nums[i] = nums[left]
                # nums[left] = tmp
                # # 注意这一步
                # if left < i:
                #     left += 1
                # else:
                #     i += 1

            elif nums[i] == 2:
                # exchange with right pointer
                tmp = nums[i]
                nums[i] = nums[right]
                nums[right] = tmp

                right -= 1
            else:
                # move i pointer
                i += 1
        return nums


if __name__ == '__main__':
    a = [2, 0, 1, 0, 2]
    s = Solution()
    ret = s.sortColors(a)
    print(ret)

'''
此题真是做的辛苦，感觉有了，就差一点规律。
1. 首先总的思路是将整个列表分为0,1,2的形式，即0,0,0,0,....1,1,...,2,2,2,2。设立左右两个指针left和right，并用
第三个指针i来从头遍历这个列表
2. 三个指针的位置变动要注意：
    （1）对于left，每次nums[i] == 0时，都要进行i和left的值交换。但是交换后要注意，当i>left时，left才加1；
         否则，i += 1
         (11.18更新)
         后来复习时，我认为更恰当的方式应该是：
         对于left，当left < i时，交换二者的值，left += 1；当left >= i时，i += 1 
    （2）对于right，则不需要上面的考虑，因为i和right是相向的，所以只要nums[i] == 2，i和right的值交换完后，
         right -= 1即可。当i > right时，循环结束。
    （3）对于nums[i] == 1, 只需要 i += 1即可
'''


