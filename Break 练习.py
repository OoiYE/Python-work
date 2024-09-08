cook = "烧烤"
answer = input("螃蟹要烧烤好吃呢还是辣椒炒好呢？")
while True:
    answer = input("抱歉，错了，请重新输入（答案正确才能退出游戏）")
    if answer == cook:
        break
print("对嘛，只有烧烤才能原汁原味")