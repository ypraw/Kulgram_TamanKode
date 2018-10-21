import timeit
def concateplus(times):
    teks = ''
    for time in range(times):
        teks += "Yunindyo Prabowo "
    return teks
def concatejoin(times):
    temp = []
    for time in range(times):
        temp.append("Yunindyo Prabowo ")
    return ''.join(temp)

print(concatejoin(10))
print(concateplus(10))

print(timeit.Timer("concateplus(100)", "from __main__ import concateplus").timeit())
print(timeit.Timer("concatejoin(100)", "from __main__ import concatejoin").timeit())