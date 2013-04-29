import itertools
from nums import makeNum, digits

result = 0

def makeNum(digs, start, end):
    x = 0
    for i in range(start, end):
        x *= 10
        x += digs[i]
    return x

results = set()

def find(aLen, bLen):
    cEnd = 9 - aLen - bLen
    aEnd = cEnd + aLen
    for p in itertools.permutations(range(1, 10), aEnd):
        if p[cEnd - 1] == 5 or p[aEnd - 1] in (1, 5):
            continue
        c = makeNum(p, 0, cEnd)
        a = makeNum(p, cEnd, aEnd)
        if c % a:
            continue

        b = c // a
        bdigs = set(range(1, 10)) - set(p)
        good = True
        for d in digits(b):
            if d in bdigs:
                bdigs.remove(d)
            else:
                good = False
                break
        if good and not bdigs:
            print('%d = %d * %d' % (c, a, b))
            results.add(c)

find(1, 4)
find(2, 3)

print(sum(results))



# n = 10
# digs = list(range(1, n))
# c = 0

# for digs

# def find(len1, len2):
#     end1 = len1
#     end2 = end1 + len2

#     def perm(startAt, stopAt, fn):
#         if startAt == stopAt:
#             return fn()
#         if perm(startAt + 1, stopAt, fn):
#             return True
#         for j in range(startAt + 1, len(digs)):
#             digs[startAt], digs[j] = digs[j], digs[startAt]
#             stop = perm(startAt + 1, stopAt, fn)
#             digs[startAt], digs[j] = digs[j], digs[startAt]
#             if stop:
#                 return True

#     def forC():
#         if digs[end1 - 1] == 5:
#             return

#         c = makeNum(0, end1)

#         def forA():
#             global result
#             if digs[end2 - 1] in (1, 5):
#                 return
#             a = makeNum(end1, end2)

#             if c % a:
#                 return
#             b = c // a

#             # print(c, '=', a, '*', b)
#             bdigs = set(digs[end2:])
#             while b:
#                 b, bd = divmod(b, 10)
#                 if bd in bdigs:
#                     bdigs.remove(bd)
#                 else:
#                     return
#             if len(bdigs) != 0:
#                 return
#             print(c, '=', a, '*', c // a)
#             result += c
#             return True
#         perm(end1, end2, forA)

#     perm(0, end1, forC)
#     assert(digs == list(range(1, 10)))
# find(4, 2)
# find(5, 2)
# find(5, 1)
# print(result)