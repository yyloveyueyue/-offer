# -*- coding:utf-8 -*-

def pro(l):
    if len(l) < 3:
        return 0
    l = sorted(list(map(int, l.split())))
    # 使用了sorted内置函数，时间复杂度上排序是达不到要求的，但是还是AC了
    return max(l[-1] * l[-2] * l[-3], l[-1] * l[0] * l[1])


def product(l):
    if len(l) < 3:
        return 0
    m, n, x, y, z = 0, 0, 0, 0, 0  # 变量常数个O(1)
    l = list(map(int, l.split()))
    for i in l:  # 循环次数是符合时间复杂度的O(n)，虽然每次循环中都比较了多次
        if i == 0:
            continue
        elif i > m:
            x = n  # 最大值改变，次大值会跟着改变
            n = m
            m = i
        elif i > n:
            x = n
            n = i
        elif i > x:
            x = i
        elif i < z:
            y = z
            z = i
        elif i < y:
            y = i
    return max(m * n * x, m * y * z)


if __name__ == "__main__":
    # n = input()
    l = input()
    print(product(l))