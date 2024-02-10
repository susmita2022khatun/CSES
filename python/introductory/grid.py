DIR_LEN = 4
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
PATH_LEN = 48
GRID_SIZE = 9
onPath = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

def tryPath(pathIdx, curR, curC):
    global onPath
    
    if (onPath[curR][curC - 1] and onPath[curR][curC + 1]) and \
       (not onPath[curR - 1][curC] and not onPath[curR + 1][curC]):
        return 0
    if (onPath[curR - 1][curC] and onPath[curR + 1][curC]) and \
       (not onPath[curR][curC - 1] and not onPath[curR][curC + 1]):
        return 0

    if curR == 7 and curC == 1:
        if pathIdx == PATH_LEN:
            return 1
        return 0

    if pathIdx == PATH_LEN:
        return 0

    ret = 0
    onPath[curR][curC] = True

    if p[pathIdx] < 4:
        nxtR = curR + dr[p[pathIdx]]
        nxtC = curC + dc[p[pathIdx]]
        if not onPath[nxtR][nxtC]:
            ret += tryPath(pathIdx + 1, nxtR, nxtC)
    else:
        for i in range(DIR_LEN):
            nxtR = curR + dr[i]
            nxtC = curC + dc[i]
            if not onPath[nxtR][nxtC]:
                ret += tryPath(pathIdx + 1, nxtR, nxtC)

    onPath[curR][curC] = False
    return ret

if __name__ == "__main__":
    line = input()

    p = []
    for cur in line:
        if cur == 'U':
            p.append(0)
        elif cur == 'R':
            p.append(1)
        elif cur == 'D':
            p.append(2)
        elif cur == 'L':
            p.append(3)
        else:
            p.append(4)

    for i in range(GRID_SIZE):
        onPath[0][i] = True
        onPath[8][i] = True
        onPath[i][0] = True
        onPath[i][8] = True

    for i in range(1, 8):
        for j in range(1, 8):
            onPath[i][j] = False

    startIdx = 0
    startR = 1
    startC = 1
    ans = tryPath(startIdx, startR, startC)
    print(ans)
