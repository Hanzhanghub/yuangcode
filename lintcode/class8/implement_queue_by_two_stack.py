# coding:utf-8

'''
date: 2017/11/20
content:
正如标题所述，你需要使用两个栈来实现队列的一些操作。
队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。
pop和top方法都应该返回第一个元素的值。

样例
比如push(1), pop(), push(2), push(3), top(), pop()，你应该返回1，2和2
'''

class MyQueue:
    def __init__(self):
        """
        @param: element: An integer
        @return: nothing
        """
        self.push_stack = []


    def push(self, element):
        """
        @return: An integer
        """
        self.push_stack.append(element)

    def pop(self):
        """
        @return: An integer
        """
        '''Solution 1: Directly using list operation'''
        # return self.push_stack.pop(0)

        '''Solution 2: High relate to the question'''
        pop_stack = []
        for i in range(len(self.push_stack)):
            pop_stack.append(self.push_stack.pop())

        ret = pop_stack.pop()

        for i in range(len(pop_stack)):
            self.push_stack.append(pop_stack.pop())
        return ret

    def top(self):
        if self.push_stack:
            return self.push_stack[0]

if __name__ == '__main__':
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    my_queue.push(5)
    # print(my_queue.top())
    print(my_queue.pop())
    print(my_queue.pop())
    my_queue.push(6)
    my_queue.push(7)
    my_queue.push(8)
    my_queue.push(9)
    print(my_queue.pop())
    print(my_queue.pop())

'''
1.这道题的考点在于怎么使用两个stack的数据结构来进行queue的pop操作
    (1)这里，两个stack，第一个push_stack的元素全部出栈，push进第二个pop_stack中，
    （2）然后pop_stack弹出末端元素，即为queue应pop出的第一个元素
    （3）最后再用for循环，将pop_stack中的元素弹出，push进push_stack中
'''
