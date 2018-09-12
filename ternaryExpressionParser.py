def parse(e):    
...     if len(e)==1:
...         return e
...     i = e.rfind('?')
...     c = e[i-1]
...     v1 = e[i+1]
...     v2 = e[i+3]
...     if c=='T':
...         v=v1
...     else:
...         v=v2
...     return parse(e[:i-1]+v+e[i+4:])
