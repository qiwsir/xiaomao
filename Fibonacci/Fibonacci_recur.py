#-*-   coding:utf-8   -*-
'''
递归法求斐波那契数列
'''
fib_seq = []
a = int(input("请输入你想获得的fibonacci数列的项数："))
for i in range(a+1):
    def f(i):
        if i == 0:
            return 0
        elif i == 1 or i == 2:
            return 1
        else:
            return f(i-1)+f(i-2)
    fib_seq.append(f(i))
print(f'斐波那契数列的前{a}项为：{fib_seq}')
