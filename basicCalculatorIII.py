def c2(s):
    st = []
    res=0
    num=0   
    prevSign = '+' 
    s = s+'+'
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = num*10 + int(s[i])
        elif s[i] in ('+','-','*','/'):
            if prevSign == '+':
                st.append(num)
            elif prevSign == '-':
                st.append(-num)
            elif prevSign == '*':
                prevNum = st.pop()
                res = prevNum * num
                st.append(res)
            elif prevSign == '/':
                prevNum = st.pop()
                res = prevNum / num
                st.append(res)
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
    return sum(st)
