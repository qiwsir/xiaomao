#-*-   coding:utf-8   -*-
'''
随机生成正态分布数据并求样本呢的期望和方差
'''
import numpy as np
def normal(u, sig):
    random_1 = np.random.normal(u, sig, 100)
    mean = np.mean(random_1)
    var = np.var(random_1)
    return mean, var
print(f'随机生成的N(5,10)样本的均值与方差分别为{normal(5, 10)}')

'''
随机生成二项分布数据并求样本的期望和方差
'''
def binomial(n, p):
    random_2 = np.random.binomial(n, p, 100)
    mean = np.mean(random_2)
    var = np.var(random_2)
    return mean, var
print(f'随机生成的B(50,0.5)的均值与方差分别为{binomial(50, 0.5)}')

'''
随机生成几何分布数据并求样本期望和方差
'''
def geometric(p):
    random_3 = np.random.geometric(p, 100)
    mean = np.mean(random_3)
    var = np.var(random_3)
    return mean, var
print(f'随机生成的Ge(0.2)样本的均值与方差分别为{geometric(0.2)}')

'''
随机生成指数分布数据据并求样本期望和方差
'''
def exponential(lamda):   ## 避免使用lambda为参数名称，因为在python里面，lambda是一个关键词，参见lambda函数
    random_4 = np.random.exponential(lamda, 100)
    mean = np.mean(random_4)
    var = np.var(random_4)
    return mean, var
print(f'随机生成的E(5)样本的均值与方差分别为{exponential(5)}')

'''
随机生成泊松分布
'''
def poisson(lamda):
    random_5 = np.random.poisson(lamda, 100)
    mean = np.mean(random_5)
    var = np.var(random_5)
    return mean, var
print(f'随机生成的P(5)样本的均值与方差分别为{poisson(5)}')
