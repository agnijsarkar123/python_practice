def not_Three(n):
    result = []
    for i in range(n+1):
        if i % 3 != 0 and i % 10 != 0:
            result.append(i)
        print(",".join(map(str, result)))
not_Three(20)
#Sir done