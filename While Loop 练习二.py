import time 
hp = 60
print("东皇太一被蜡笔小新的动感光波击中，血量还剩" + str(hp))
print("东皇太一使用补单！")
while hp < 100:
    time.sleep(2)
    hp += 10 
    print("东皇太一的 血量 + 10hp 为" + str(hp))
print("东皇太一血量已满！")