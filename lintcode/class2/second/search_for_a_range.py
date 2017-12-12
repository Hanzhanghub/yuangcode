# coding:utf-8

'''
date: 2017/12/11
content:
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。
如果目标值不在数组中，则返回[-1, -1]

样例
给出[5, 7, 7, 8, 8, 10]和目标值target=8,
返回[3, 4]
'''


class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # special condition
        if not A:
            return [-1, -1]

        start, end = 0, len(A) - 1
        index1, index2 = -1, -1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] == target:
                # more operation
                # if index1 == -1:
                #     while mid - 1 > start and A[mid] == A[mid - 1]:
                #         mid -= 1
                #     index1 = mid
                #     mid = start + (end - start) // 2
                # start = mid
                index1, index2 = mid, mid
                break
            elif A[mid] < target:
                start = mid
            else:
                end = mid


        while index1 - 1 >= start and A[index1] == A[index1 -1]:
            index1 -= 1

        while index2 + 1 <= end and A[index2] == A[index2 +1]:
            index2 += 1




        if A[start] == target:
            index1 = start if index1 == -1 else index1
            index2 = start if index2 == -1 else index2
        if A[end] == target:
            index1 = end if index1 == -1 else index1
            index2 = end if index2 < end else index2

        return [index1, index2]


if __name__ == '__main__':
    s = Solution()
    ret = s.searchRange([5, 7, 7, 8, 8, 10], 10)
    print(ret)


'''
1.我的解法虽然能过，但是我觉得有点乱：
    （1）使用二分法，找到target，就break。然后分别从这个mid的左边和右边循环找到边界。
    （2）同时需要考虑极端的情况：即二分退出时还没有找到target
2.给出的标准答案是做两次二分：
    （1）第一次end = mid，找到最左边的index1
    （2）第二次start = mid，找到最右边的index2
'''