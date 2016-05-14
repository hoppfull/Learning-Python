for i in range(10):
    if(i < 7):
        if(i%2 == 0):
            print(i)
            print("i is even!")

for i in range(10):
    if(not(i <7)):
        continue
    if(not(i%2 == 0)):
        continue
    print(i)
    print("i is even!")
    
#continue basicly means "skip rest and continue with loop" It's good to avoid deeply nested loops and can make it easier to optimize the code becouse you'll easier see which if-statements you can remove