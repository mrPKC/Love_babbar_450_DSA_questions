def commonElements(a, b, c, n1, n2, n3):
    # your code here
    i = j = 0
    op = []
    while(i < n1 and j < n2):
        if(a[i] == b[j] and len(op) == 0):
            op.append(a[i])
            i += 1
            j += 1
        elif(a[i] == b[j] and a[i] != op[-1]):
            op.append(a[i])
            i += 1
            j += 1
        elif(a[i] < b[j]):
            i += 1
        else:
            j += 1
    if(len(op) == 0):
        return [-1]
    else:
        i = j = 0
        op2 = []
        while(i < len(op) and j < n3):
            if(op[i] == c[j] and len(op2) == 0):
                op2.append(op[i])
                i += 1
                j += 1
            elif(op[i] == c[j] and op[i] != op2[-1]):
                op2.append(op[i])
                i += 1
                j += 1
            elif(op[i] < c[j]):
                i += 1
            else:
                j += 1
        if(len(op2) == 0):
            return [-1]
        else:
            return op2


print(commonElements([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [
      3, 4, 15, 20, 30, 70, 80, 120], 6, 5, 8))
