def c(s):
    st = []
    prevSign = '+'
    num = 0
    for i in s+'+':
        if i.isdigit():
            num = num*10 + int(i)
        elif i!=' ': #it's a sign.
            if prevSign=='+':
                st.append(num)
            elif prevSign=='-':
                st.append(-num)
            elif prevSign=='*':
                prevNum = st.pop()
                res = prevNum * num
                st.append(res)
            elif prevSign=='/':
                prevNum = st.pop()
                res = prevNum / num
                st.append(res)
            prevSign = i
            num=0
    return sum(st)
