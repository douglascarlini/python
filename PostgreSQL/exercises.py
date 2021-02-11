
# fibonach sequence
# def fibo(n): return n if n < 2 else (fibo(n-1) + fibo(n-2))
# for i in range(10): print(fibo(i))

# factorial
# def fact(n): return 1 if n < 1 else n * fact(n-1)
# print(fact(0))




# binary search tree
def bst(vals, side='M', deep=0):

    if not vals:
        return None
    mid = len(vals)//2 # rounded division (floor)
    print("Node[{}{}]: {} <{}> {}".format(side, deep, vals[:mid], vals[mid], vals[mid+1:]))
    return vals[mid], bst(vals[:mid], 'L', deep+1), bst(vals[mid+1:], 'R', deep+1)

bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])