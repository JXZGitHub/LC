
def uneaten_brute_force(n,a):
    """
    Given number n (leaves), and list a of integers (all caterpiller's 'a numbers').
    Return the number of elements from 1 to N (inclusive) that can are NOT multiples of any number in A.
    ie : "a caterpillar will eat a leaf that is a mulitple of any of its 'a numbers', return the number of uneaten leaves"

    1<=N<=1000000000
    2<=len(A)<=20
    A is sorted.
    """
    eaten = 0
    for leaf in range(1, n + 1):  # This double loop makes it O(n*len(a))
        for factor in a:
            if leaf % factor == 0: #Leaf is a multipler of factor
                eaten +=1
                break

    return n-eaten

def uneaten_optimized(n,a): #It can reduce a into mutually undivisible factors, but only works if a is reducible.
    """
    Given number n (leaves), and list a of integers (all caterpiller's 'a numbers').
    Return the number of elements from 1 to N (inclusive) that can are NOT multiples of any number in A.
    ie : "a caterpillar will eat a leaf that is a mulitple of any of its 'a numbers', return the number of uneaten leaves"
    """
    eaten = 0

    #reduces a into a smaller list.
    reduced_factors = [a[0]]
    for i in range(1,len(a)):
        for reduced in reduced_factors:
            if a[i] % reduced == 0:
                break
        else:
            reduced_factors.append(a[i])



    return n-eaten

print (uneaten_brute_force(7,[2,3,4,5,6,7]))
print (uneaten_optimized(7,[2,3,4,5,6,7]))

print (uneaten_brute_force(10,[2,3,5]))
print (uneaten_optimized(10,[2,3,5]))

print (uneaten_brute_force(10, [2,4,5,10]))
print (uneaten_optimized(10, [2,4,5,10]))

print (uneaten_optimized(20, [2,3,5]))
print (uneaten_brute_force(20, [2,3,5]))

#print (uneaten_optimized(1000000000, [2,3,5]))
