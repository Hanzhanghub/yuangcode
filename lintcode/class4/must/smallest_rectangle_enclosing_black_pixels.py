# coding:utf-8

'''
date:2017/10/10
content:
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. 
The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. 
Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that 
encloses all black pixels.
For example, given the following image:

[
"0010",
"0110",
"0100"
]
and x = 0, y = 2,
Return 6.
'''
class Solution(object):
    def smallest_rectangle_enclosing_black_pixels(self,image,x,y):
        # special
        if not image:
            return 0

        # construct a dictionary to store coordinate x and coordinate y
        result = []
        result.append((x,y))

        #
        DIRECTION =4
        delta_x = [1,0,0,-1]
        delta_y = [0,1,-1,0]

        # BFS
        queue = []
        queue.append((x,y))

        while queue:
            pop_coor = queue.pop(0)
            for i in range(DIRECTION):
                next_x, next_y = pop_coor[0] + delta_x[i], pop_coor[1] + delta_y[i]
                if self.isNotBound(image, next_x, next_y):
                    if (next_x, next_y) not in result:
                        queue.append((next_x,next_y))
                        result.append((next_x,next_y))

        print(result)

        # statics
        length = max([x[0] for x in result]) - min([x[0] for x in result]) + 1
        weight = max([x[1] for x in result]) - min([x[1] for x in result]) + 1
        return length * weight

    def isNotBound(self,image,x,y):
        row = len(image)
        line = len(image[0])
        if x >=0 and x<row and y>=0 and y<line and image[x][y] ==1 :
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    ret = s.smallest_rectangle_enclosing_black_pixels(image=[
        [1,1,1,0],
        [0,1,1,1],
        [0,1,0,0]],
        x=0,y=2)
    print(ret)

'''
1.矩阵的bfs基本已经掌握。
    1.建立映射表
    2.从何处开始---此题已给出开始点，只需要bfs找到所有的1
    3.记录已遍历过的点
    4.何时入队、出队
'''