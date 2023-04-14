

F4 = float(input("F4:"))
F200 = float(input("F200:"))
try:
    PL = float(input("PL:"))
    LL = float(input("LL:"))
    CU = float(input("Cu:"))
    CC = float(input("Cc:"))

    PIs = LL-PL
    PIa = 0.73*(LL-20)
except:
    pass


if F200 > 50:
    
    if PIs > PIa:
        first_C = "C"
        if LL > 50:
            sec_C = "H"
        else:
            sec_C = "L"
    else:
        first_C = "M"
    
    name = first_C + sec_C
    print(name)
else:
    if 100 - F4 > F4 - F200:
        first_C = "G"
    else:
        first_C = "S"

    if F200 < 5:
        if first_C == "G":
            if CU >= 4 and CC <=3 and CC >= 1:
                sec_C = "W"
            else:
                sec_C = "P"
        else:
            if CU >= 6 and CC <=3 and CC >= 1:
                sec_C = "W"
            else:
                sec_C = "P"
        print(first_C + sec_C)
    elif F200 > 12:
        
        if PIs > PIa:
            sec_C = "C"
        else:
            sec_C = "M"
        print(first_C+sec_C)
    else:
        if 100 - F4 > F4 - F200:
            first_C = "G"
        else:
            first_C = "S"
        
        if first_C == "G":
            if CU >= 4 and CC <=3 and CC >= 1:
                sec_C = "W"
            else:
                sec_C = "P"
        else:
            if CU >= 6 and CC <=3 and CC >= 1:
                sec_C = "W"
            else:
                sec_C = "P"
        if PIs > PIa:
            third_C = "C"
            if LL > 50:
                four_C = "H"
            else:
                four_C = "L"
        else:
            third_C = "M"
        
        print(first_C+sec_C+"-"+third_C+four_C)
