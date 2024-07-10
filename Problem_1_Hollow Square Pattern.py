#hollow square pattern

for i in range(5):  #user variable input 
    for j in range(5):
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
            print('*', end='')
        else:
            print('', end=' ')
    print() 