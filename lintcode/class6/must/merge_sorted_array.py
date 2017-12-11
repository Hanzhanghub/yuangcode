# coding:utf-8

'''
date: 2017/11/8
content:
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Notice
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. 
The number of elements initialized in A and B are m and n respectively.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
'''


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # special condition
        if not A and not B:
            return A

            # put B into A
        A[m:] = B

        # sort A using quick sort
        self.quick_sort(A, 0, len(A) - 1)

        return A

    def quick_sort(self, a, start, end):
        if start >= end:
            return

        # set pivot
        mid = (start+end) // 2
        pivot = a[mid]
        left = start
        right = end

        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1

            while left <= right and a[right] > pivot:
                right -= 1

            if left <= right:
                # change value of left and right
                tmp = a[right]
                a[right] = a[left]
                a[left] = tmp
                right -= 1
                left += 1

        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)

if __name__ == '__main__':
    a = [1, 2, 3, None, None]
    b = [4, 5]
    s = Solution()
    ret = s.mergeSortedArray(a,3,b,2)
    print(ret)

'''
1.开头的思路：由于A的数组大小确定是m+n，所以先把B插入A中empty的地方，即A[m:] = B
2.接着对A进行快速排序即可。
'''

