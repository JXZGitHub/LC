def c2(s):
    res=0
    num=0   
    prevSign = '+' 
    s = s+'+'
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = num*10 + int(s[i])
        elif s[i] in ('+','-'):
            if prevSign == '+':
                res += num
            elif prevSign == '-':
                res -= num
            num=0
            prevSign = s[i]
        elif s[i] in ('('):
            j=i
            cnt = 0
            while i<len(s):
                if s[i]=='(':
                    cnt +=1
                if s[i]==')':
                    cnt -=1
                if cnt==0:
                    break
                i+=1
            num = c2(s[j+1:i])
        i += 1
    return res
