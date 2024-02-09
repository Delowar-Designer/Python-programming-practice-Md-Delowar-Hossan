# write a prigram to calculate summation of add number from 1-100 in python
def summation():
    sum=0
    for i in range(100):
        if i%2!=0:
            sum=sum+i
    print("Result= ",sum)
summation()