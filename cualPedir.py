def maximo(l):
    max = l[0]
    c = 0
    inx = 0
    for x in l:
        if x > max:
            max = x
            inx = c
        c += 1
    return inx

def pide(l):
    A1 = 0
    B1 = 0
    C1 = 0
    D1 = 0
    A2 = 0
    B2 = 0
    C2 = 0
    D2 = 0
    A3 = 0
    B3 = 0
    C3 = 0
    D3 = 0
    A4 = 0
    B4 = 0
    C4 = 0
    D4 = 0
    p1 = l[0]
    for c in p1:
        if c[0] == "A":
            A1 += 1
        elif c[0] == "B":
            B1 += 1
        elif c[0] == "C":
            C1 += 1
        elif c[0] == "D":
            D1 += 1

    for j in range(1,4):
        px = l[j]
        for c in px:
            if j == 1:
                if c[0] == "A":
                    A2 += 1
                elif c[0] == "B":
                    B2 += 1
                elif c[0] == "C":
                    C2 += 1
                elif c[0] == "D":
                    D2 += 1
            elif j == 2:
                if c[0] == "A":
                    A3 += 1
                elif c[0] == "B":
                    B3 += 1
                elif c[0] == "C":
                    C3 += 1
                elif c[0] == "D":
                    D3 += 1
            elif j == 3:
                if c[0] == "A":
                    A4 += 1
                elif c[0] == "B":
                    B4 += 1
                elif c[0] == "C":
                    C4 += 1
                elif c[0] == "D":
                    D4 += 1

    if (A1 == 4 or B1 == 4 or C1 == 4 or D1 == 4):
        print("Ya no puedes pedir más")
        return -1, -1

    palosdej1 = [A1,B1,C1,D1]
    max1 = maximo(palosdej1)
    paloA = [A2, A3, A4]
    paloB = [B2, B3, B4]
    paloC = [C2, C3, C4]
    paloD = [D2, D3, D4]

    jp = 0

    if max1 == 0:
        pp = paloA[0]
        c = 2
        for x in paloA:
            if x >= pp:
                pp = x
                jp = c
            c += 1
        return "A", jp
    elif max1 == 1:
        pp = paloB[0]
        c = 2
        for x in paloB:
            if x >= pp:
                pp = x
                jp = c
            c += 1
        return "B", jp
    elif max1 == 2:
        pp = paloC[0]
        c = 2
        for x in paloC:
            if x >= pp:
                pp = x
                jp = c
            c += 1
        return "C", jp
    elif max1 == 3:
        pp = paloD[0]
        c = 2
        for x in paloD:
            if x >= pp:
                pp = x
                jp = c
            c += 1
        return "D", jp
