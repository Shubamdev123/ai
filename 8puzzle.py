from collections import deque
def prints(board):
    for i in range(0,9,3):
        print(board[i:i+3])
    print()

def moves(zindex):
    m=[]
    if zindex>=3:
        m.append(zindex-3)
    if zindex<6:
        m.append(zindex+3)
    if zindex%3>0:
        m.append(zindex-1)
    if zindex%3<2:
        m.append(zindex+1)
    return m

def swap(board,p1,p2):
    b=board[:]
    b[p1],b[p2]=b[p2],b[p1]
    return b

def bfs(s,g):
    v=set()
    q=deque([(s,[])])
    v.add(tuple(s))
    while q:
        board,path=q.popleft()
        if board==g:
            return path + [board]
        zindex=board.index(0)
        for move in moves(zindex):
            b=swap(board,zindex,move)
            if tuple(b) not in v:
                v.add(tuple(b))
                q.append((b,path + [board]))
    return None

s=[1,2,3,4,5,6,7,8,0]
g=[1,2,0,4,5,6,7,3,8]
res=bfs(s,g)
if res:
    print("solution found")
    for i in res:
        prints(i)
else:
    print("no solution found")  