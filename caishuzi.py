import random as r
a= r.randint(0,100)
for i in range(6):
             b=int(input("请输入一个0到100的正整数："))
             if b<a:
                          print("猜小了，共10次机会，还剩{}次".format(5-i))
             elif b>a:
                          print("猜大了，共10次机会，还剩{}次".format(5-i))
             else:
                          print("猜对了，该数字为{}".format(a))
             while i == 9:
                          print("机会已用尽，您并没有猜出数字，游戏结束")
                          break


