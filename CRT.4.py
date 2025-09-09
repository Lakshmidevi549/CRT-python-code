#write the python progrom to print even number from n to 1
n=int(input('Enter the interger value:'))
print(f"Natural numbers from 1 to n {n}:")
for i in range(n,0,-1):
    if(i%2==0):
        print(i)