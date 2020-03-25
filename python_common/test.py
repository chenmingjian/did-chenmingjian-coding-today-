
# def main():
#     n = raw_input()
#     print(n)
#     matrix = []
#     for i in range(3):
#         matrix.append(raw_input())
#     matrix = [list(map(int,i.split(' '))) for i in matrix]
#     matrix = [[i, j, k] for i, j, k in zip(matrix[0],matrix[1],matrix[2])]
#     print(matrix)

#     for i in range(matrix[1]):
def main():
    line = input()
    n, m, q = (int(i) for i in line.split(' '))

    matrix = []
    for i in range(n):
        matrix.append(input())
    matrix = [list(map(int,i.split(' '))) for i in matrix]
    # n = 3
    # m = 3
    # matrix = [[1, 0, 3], [0, 0 ,0], [7, 0, 9]]
    Q = []
    for i in range(q):
        Q.append(input())
    Q = [list(map(int,i.split(' '))) for i in Q]

    for i in range(n):
        r = [matrix[i][j] for j in range(m)]
        if r.count(0) + 2 <= m:
            info = []
            for idx, num in enumerate(r):
                if num != 0:
                    info.append([idx, num])
                if len(info) == 2:
                    break
            res = (info[1][1] - info[0][1]) / (info[1][0] - info[0][0])
            for j in range(m):
                if matrix[i][j] == 0: 
                    
                    matrix[i][j] = info[0][1] + (j - info[0][0]) * res
    for j in range(m):
        c = [matrix[i][j] for i in range(n)]
        if c.count(0) + 2 <= n:
            info = []
            for idx, num in enumerate(c):
                if num != 0:
                    info.append([idx, num])
                if len(info) == 2:
                    break
            res = (info[1][1] - info[0][1]) / (info[1][0] - info[0][0])
            for i in range(n):
                if matrix[i][j] == 0: 
                    matrix[i][j] = info[0][1] + (i - info[0][0]) * res
    for i, j in Q:
        if matrix[i-1][j-1] != 0:
            print(int(matrix[i-1][j-1]))
        else:
            print("Unknown")
    # print(matrix)
    



if __name__ == '__main__':
    main()