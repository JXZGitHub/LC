#https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=501860

# 给一个矩阵
# 类似这样的
# [[0, 0, 1, 1, 1],
# [0, 1, 1, 1, 1],
# [0, 0, 1, 1, 1],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 1, 1]]
# 1. 每一个cell 要不是0 要不是1
# 2. 每一行只要发现一个1， 剩下的都是1
# 3. 这个数组是正方形的
# 问题：找到最左边的有1的列
# 这个例子的结果是第二列(column): return 1 (index of 2nd column).

def leftMostColumn(m):
    '''
    :param m:
    :return:
    Time: O(M*N)
    Space: (1)
    '''
    row = 0
    col = len(m[0]) - 1
    while row<len(m):
        while col>0 and m[row][col-1] == 1:
            col -= 1
        row +=1
    return col

m = [[0,0,0,0,1],[0,0,1,1,1],[0, 0, 1, 1, 1],[0, 0, 0, 0, 0],[0, 0, 0, 1, 1]]
m2 = [[0,0,0,0,0],[0,0,0,1,1]]
m3 = [[0,1],[1,0]]
print (leftMostColumn(m3))


