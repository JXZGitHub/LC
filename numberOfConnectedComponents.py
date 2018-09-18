def cc(g):
    p={}
    r={}    
    for (a,b) in g:
        print 'procesing', a, b
        pA=find(a,p)
        pB=find(b,p)   
        if pA!=pB:
            res -= 1
            ##Union by rank , parent (set) with smaller rank joins bigger rank.
            rA=r.setdefault(pA,0)
            rB=r.setdefault(pB,0)
            if rA == rB:
                r[pB] = rB+1 #Same ranks joined, resulting set has +1 rank.
            elif rA>rB: #Ensures smaller rank joins bigger rank.
                pA,pB=pB,pA

            print 'setting ' + str(pA) + 's parent to be ' + str(pB)
            p[pA]=p[pB]
    res = set()

    for n in p.keys():
        res.add(find(n,p))
 
    print res,p
    print len(res)

def cc2(g):
    p=collections.defaultdict(list)
    v=set()
    res = 0
    for (a,b) in g:        
        p[a].append(b)
        p[b].append(a)
    for n in p:
        if n not in v:
            res +=1
            rec(n,p,v)
    print res

def rec(n,p,v):
    if n in v:
        return
    v.add(n)
    for c in p[n]:
        rec(c,p,v) 
