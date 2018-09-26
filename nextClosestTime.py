def nct2(t):
    #import collections
    totalMins = 60*24
    #s=collections.Counter(t)
    s=set(t)
    currentMin = int(t[:2])*60 + int(t[3:])
    for i in range(1,totalMins+1):        
        timeToTry = (currentMin + i) % totalMins
        hh,mm = divmod(timeToTry,60)
        time = '{:02d}'.format(hh) + ':' + '{:02d}'.format(mm)        
        if set(time) <= s:
            return time
        
        #if collections.Counter(time) == s:
        #    return time
    return None
    
def nct(t):        
    st = set([t[0],t[1],t[3],t[4]])
    s=''.join(sorted(list(st)))   
    newTime = t    
    for i in range(len(t)-1,-1,-1):  
        size=len(s)-1
        if i==2:
            continue
        digit = t[i]
        s_index = s.find(digit)        
        if s_index==size:
            newTime = newTime[:i]+s[0]+newTime[i+1:]
            continue   
        nextNumber = s[s_index+1]
        if i==4:            
            return newTime[:i]+nextNumber+newTime[i+1:]                
        elif i==3:
            if int(nextNumber)<6:
                return newTime[:i]+nextNumber+newTime[i+1:]
        elif i==1:
            if int(newTime[0])<2 or int(nextNumber)<=3:
                return newTime[:i]+nextNumber+newTime[i+1:]
        else:
            if int(nextNumber)<=2:
                return newTime[:i]+nextNumber+newTime[i+1:]
        newTime = newTime[:i]+s[0]+newTime[i+1:]
       
    return newTime
