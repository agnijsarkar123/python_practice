def setup():
    for i in range(6):
        for j in range(5):
            print('#',end=' ') if i%2==0 else print('@',end=' ')
        print()
setup()