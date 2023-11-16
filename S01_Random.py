import random

nums = [1, 3, 5, 7, 9]
newnums = random.shuffle(nums)
print("将nums元素随机打乱", newnums)
print("随机生成一个a-b的整数：", random.randint(1, 6)) # 随机生成a-b的整数
print("随机生成一个0-1的浮点数：", random.random())  # 随机生成0到1的浮点数
print("随机生成一个a-b的浮点数：", random.uniform(0.01, 5.56))
print("从序列中随机取一个字符：")
print( random.choice("hello world"))
print (random.choice(["python", "tab", "com"]))
print("从序列中随机取一个字符：", random.choices("hello world"))
print("从a-b中随机取间隔为c的数：", random.randrange(1, 100, 3)) # 步长3例如从1， 4， 7
print("多个字符中随机生成指定数量的字符串", random.sample('zyxwvutsrqponmlkjihgfedcba',5))
