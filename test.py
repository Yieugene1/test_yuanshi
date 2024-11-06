#第一题1.大量的URL字符串，如何从中去除重复的，优化时间空间复杂度

def rmv_urls(urls):
    return list(set(urls))

#第一题test case:
urls = [
        "https://1.com",
        "https://2.com",
        "https://3.com",  
        "https://1.com",
        "https://2.com", 
        "https://3.com"
    ]
result = rmv_urls(urls)
print(result)

#第二题 python实现单例模式
class single:
    _ins=None
    def __new__(cls, *args, **kwargs):
        if not cls._ins:
            cls._ins = super(single, cls).__new__(cls, *args, **kwargs)
        return cls._ins

#第二题test case:
class1 = single()
class2 = single()
print(id(class1))
print(id(class2))
print(class1 is class2)

#第三题定义栈的数据结构，要求添加一个min函数，能够得到栈的最小元素。 
# 要求函数min、push以及pop的时间复杂度都是O(1)。

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        
        self.stack.append([val, min_val])

    def pop(self):
        return self.stack.pop()[0] if self.stack else None

    def top(self):
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        return self.stack[-1][1] if self.stack else None

#test case :

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(-1)
stack.push(4)
print(stack.top())
print(stack.getMin())