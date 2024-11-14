def patt():
    ch = 65
    for i in range(6):
        for j in range(4):
            if j % 2 == 0:
                print(chr(ch),end = " ")
            else:
                print(chr(ch+32),end = " ")
            ch =ch+1
        print()
patt()