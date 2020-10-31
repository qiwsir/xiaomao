#-*-   coding:utf-8   -*-
'''
生成器求斐波那契数列
'''
def fib():
    n = int(input("请输入你想获得的斐波那契数列的项数："))
    fib_num1 = 0
    fib_num2 = 1
    for i in range(n+1):
        '''将函数制作成生成器'''
        yield fib_num1
        fib_num1, fib_num2 = fib_num2, fib_num1 + fib_num2

'''调用生成器'''
flag = True
for fib_item in fib():
    if flag:
        print(f"由生成器生成的斐波那契数列为：", end=" ")
        flag = False
    print(fib_item, end=" ")