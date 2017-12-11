# coding:utf-8

'''
date:2017/11/9
content:
返回两个数组的交

注意事项
Each element in the result must be unique.
The result can be in any order.

样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].
'''


class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):

        ''' solution 1: merge two sorted array'''
        # step 1: sort two arrays
        nums1.sort()
        nums2.sort()

        # step 2: search the same number
        ret = set([])
        lstart, rstart = 0, 0
        lend,rend = len(nums1) - 1, len(nums2) - 1

        while lstart <= lend and rstart <= rend:
            if nums1[lstart] < nums2[rstart]:
                lstart += 1
            elif nums1[lstart] == nums2[rstart]:
                ret.add(nums1[lstart])
                lstart += 1
                rstart += 1
            else:
                rstart += 1
        return list(ret)

if __name__ == '__main__':
    a = [1,2,2,1]
    b = [2,2]
    s = Solution()
    ret = s.intersection(a,b)
    print(ret)

'''
1.解法一：将两个列表排好序，用两个指针分别从头对两排序列表比较，相同的则为交集 --- merge two sorted array 
2.解法二：hash map（待补充）
3.解法三；（待补充）
'''