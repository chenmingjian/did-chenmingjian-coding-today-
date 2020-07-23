'''
2
6
3 7 1 4 1 2
3 7 3 6 3 2
5
1 1 1 1 1
1 2 1 3 1

1
10000

'''
import sys
def main1():
    def ok(a, b):
        diff = []
        for i, j in zip(a, b):
            diff.append(j - i)
        # print(diff)
        while diff and diff[0] == 0:
            diff.pop(0)
        while diff and diff[-1] == 0:
            diff.pop()
        # print(diff)
        if 0 in diff:
            print("NO")
            return
        squeeze_diff = []
        constans = 1
        for i in diff:
            if i == 0:
                continue

            squeeze_diff.append(i)
        else:
            print ("YES" if len(set(squeeze_diff)) == 1 else "NO")
    t = int(input())
    ans = 0

    A, B = [], []
    for i in range(t):
        n = int(input().strip())

        line = input().strip()
        a = list(map(int, line.split()))
        A.append(a)
        line = input().strip()
        b = list(map(int, line.split()))
        B.append(b)


    for aa, bb in zip(A, B):
        ok(aa, bb)

"""
3 4
50 100 200
99 199 200 300
"""
def main3():
    _ = input()

    ticket = list(map(int, input().split()))
    goods = list(map(int, input().split()))

    ans = 0
    set_ticket = set(ticket)
    a = sorted(ticket + goods)

    this = 0
    for i in a:
        if i in set_ticket:
            this = i
        ans += i - this
    print(ans)
main3()

"""
3
4
1 4 3 3
5
8 2 2 4 6
6
5 8 1 3 2 9
"""
def main4():
    t = int(input())
    l = []
    for i in range(t):
        _ = input()
        l.append(list(map(int, input().split())))
    def ok(hl):
        ans = []
        for i, h in enumerate(hl):
            #left check
            count = 0
            for c in hl[0:i][::-1]:
                if c <=h:
                    count+=1 
                else:
                    break
            for c in hl[i+1:]:
                if c <=h:
                    count+=1 
                else:
                    break
            ans.append(count)
        return ''.join([ str(i) + " " for i in ans])
    for i in l:
        print(ok(i)[:-1])
            
    
# def main2():
#     n = int(input())
#     ss = list(map(int, input().split()))

#     for k in sorted(d.keys):
#         index = d[k]
#         for i in ss[:index-1][::-1]:
#             if 
# main3()