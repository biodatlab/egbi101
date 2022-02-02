def pattern5(n):
    for i in range(n, 0, -1):
        print("X " * (i-1) , end="")
        for j in range(i, n+1):
            print(str(j)+" ",end="")
        print()