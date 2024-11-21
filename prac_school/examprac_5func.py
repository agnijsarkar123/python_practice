def setup():
    x=97
    for i in range(1,5):
        for j in range(1,6):
            print(chr(x),end=', ')
            x=x+1
        print()
setup()
