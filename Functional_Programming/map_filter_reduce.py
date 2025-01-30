from functools import reduce

number=[1,2,3,4,5,6,7,8,9,10]

squared=list(map(lambda x:x*x,number))

print(f"Squared numbers are : {squared}")

even=list(filter(lambda a:a%2==0,number))

print(f"Even numbers are : {even}")

totalSum=reduce(lambda a,b:a+b,number,-50)

print(f"Total sum is : {totalSum}")