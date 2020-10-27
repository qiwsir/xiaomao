import random

a= random.randint(0,100)#随机产生一个0到100的整数
for i in range(10):
    b=input("请输入一个0到100的正整数：")#用户获取一个输入
    if b.isnumeric():
        if int(b)>=0 and int(b)<=100:
            if int(b)<a:
                print("猜小了，共10次机会，还剩{}次".format(9-i))
            elif int(b)>a:
                print("猜大了，共10次机会，还剩{}次".format(9-i))
            elif int(b)==a:
                print("恭喜您，猜对了，该数字为{}".format(a))
                break
            else:
                print("您并没有输入0到100的整数，浪费了一次机会")
    else:
        print("您没有输入数字，请输入0到100的整数")
    while i == 9:
        print("机会已用尽，您并没有猜出数字，游戏结束")
        break


