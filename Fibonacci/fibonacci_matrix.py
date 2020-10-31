#-*-   coding:utf-8   -*-
'''
矩阵法实现斐波那契数列
'''
import numpy as np
fib_mat = np.array([[1, 0]])
fun_mat = np.array([[1, 1], [1, 0]])
n = int(input("请输入想要获得的斐波那契数列的项数:"))
print(f'斐波那契数列的前{n}项为:', end='')
for i in range(n+1):
    if i == 0:
        print(fib_mat[0][1], end=' ')
    else:
        fib_mat = fib_mat.dot(fun_mat ** n)
        print(fib_mat[0][1], end=' ')