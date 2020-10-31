#-*-   coding:utf-8   -*-
'''
for循环实现斐波那契数列
'''
fib_seq = []
a = int(input("请输入你想获得的斐波那契数列的项数："))
for i in range(a+1):
    if i == 0:
        fib_seq.append(0)
    elif i == 1 or i == 2:
        fib_seq.append(1)
    else:
        fib_seq.append(fib_seq[i-1]+fib_seq[i-2])
print(f'斐波那契数列的前{a}项为:{fib_seq}')
