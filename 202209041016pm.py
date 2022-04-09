# 1. How to find average of n numbers?
# 2. Exit program with -1

n = 0
sum = 0
avg = 0
count = 0

while(n>=0):
    count += 1
    num = int(input("Enter a number: "))
    if(num==-1):
        break
    sum += um
    avg = sum / count
    print("SUM:",sum)
    print("AVG:",avg)