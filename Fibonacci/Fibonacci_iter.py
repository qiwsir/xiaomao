#-*-   coding:utf-8   -*-
'''
迭代器实现斐波那契数列
'''
fib_seq = []
n = int(input("请输入你想获得的斐波那契数列的项数："))    # 由于斐波那契数列含第零项为0，因而输出结果共有n+1个数字
class Fibonacci_class:
    
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.num_1 = 0
        self.num_2 = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a == 0:
            self.num_1, self.num_2 = self.num_1, self.num_2    # 判断是否是第零项（初始状态）
        elif self.a <= n+1:
            self.num_1, self.num_2 = self.num_2, self.num_1+self.num_2    # 从n=1开始叠加
        else:
            raise StopIteration    # 若超过目标项数则停止迭代，抛出异常
        self.a += 1
        return self.num_1


Fibonacci = Fibonacci_class(n)
for i in range(n+1):
    fib_seq.append(next(Fibonacci))    # 用next方法将返回结果依次放入列表中
print(f'斐波那契数列的前{n}项为:{fib_seq}')