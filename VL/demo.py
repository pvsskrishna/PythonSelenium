def func(n):
    s = str(n)
    m = int(s[0]) + int(s[-1])
    n = 0
    for i in range(1,len(s)-1):
        n += int(s[i])
    if m == n:
        return 'xylen'
    else:
        return 'not a xylen'
print(func(123456))