def gbfs(sn,stn):
    os={sn}
    cs=set()
    p={sn:sn}
    while len(sn)>0:
        n=None
        for v in os:
            if n is None or hueristic(v)<hueristic(n):
                n=v
        if n==stn:
            path=[]
            while p[n]!=n:
                path.append(n)
                n=p[n]
            path.append(n)
            path.reverse()
            pstr="-->".join(path)
            print("Path found {}".format(pstr))
            return pstr
        if n==None:
            print("path not found")
            return None
        os.remove(n)
        cs.add(n)
        for (m,w) in getn(n):
            if m not in os and m not in cs:
                os.add(m)
                p[m]=n
    print("path not found")
    return None

def getn(v):
    if v in graph:
        return graph[v]
    else:
        return None

def hueristic(n):
    hdist={
        's':5,
        'a':3,
        'b':4,
        'c':2,
        'd':6,
        'g':0,
    }
    return hdist[n]

graph={
    's':[('a',1)],
    'a':[('b',2),('c',1)],
    'b':[('d',5)],
    'c':[('d',3),('g',4)],
    'd':[('g',2)],
}

gbfs('s','g')