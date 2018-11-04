def is_valid(state, pos):
    for i in range(len(state)):
        if abs(state[i] - pos) in (0, len(state) - i):
            return False
    return True


def DFS(n, i, state, result):
    if i == n:
        tmp = []
        for i in xrange(len(state)):
            tmp.append("."*state[i]+"Q"+"."*(n-state[i]-1))
        result.append(tmp)
        return
    for pos in range(n):
        if is_valid(state, pos):
            state.append(pos)
            DFS(n, i + 1, state, result)
            state.pop()


n = 4
result = []
DFS(n, 0, [], result)
print result



