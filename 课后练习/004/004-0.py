import random
secret=random.randint(1,10)
print('---------我爱鱼c工作室-----------------')
temp=input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess=int(temp)
i=1
while guess!=secret and i<=2:
    temp=input("哎呀，猜错了，重新输入：")
    guess=int(temp)
    if guess ==secret:
        print("我艹，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励！")
    else:
        if guess>secret:
            print("哥，大了大了！")
            i=i+1
        else:
            print("猜错了，小甲鱼现在心里想的是8！")
            i=i+1
print("游戏结束了，不玩了。")

