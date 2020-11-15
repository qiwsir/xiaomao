#-*-   coding:utf-8   -*-
'''
写一个类实现由阿拉伯数字到罗马数字的转换
'''


class num_change:
    def __init__(self, n):
        self.arab = n
        self.rome = ''

    def exc(self):
        rom = '〇ⅠⅡⅢⅣⅤⅥⅦⅧⅨ'
        for i in self.arab:
            self.rome += rom[eval(i)]
        return self.rome


num = input("请输入所需转换的阿拉伯数字：")
Num_Change = num_change(num)
print(f'转换后的罗马数字为：{Num_Change.exc()}')
