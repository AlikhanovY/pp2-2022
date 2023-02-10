def fun(numh, numl):
    numср=0
    numra=0
    for i in range(1,numh+1):
        numch=i
        numra=numh-i
        if((numch*4+numra*2)==numl):
            break
    print(f"number of rabbits = {numra} and number of chicks = {numch}")

fun(35,94)