def hanoi(n, a, b, c):
    # 参数a，b，c是珠子的名称
    # 函数hanoi()表示第n个盘子，从a开始移动，经过b，最终到达c
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(f"把{n}号圆盘从{a}位置移动到啊{c}位置")
        hanoi(n - 1, b, a, c)

hanoi(3, "A", "B", "C")
