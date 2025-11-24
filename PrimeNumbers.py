a= int(input( "enter a number:"))
if a%2==1 and a%a==0 :
    print(a,'is a prime number')
else:
     print(a,'is not a prime number')
#Prime Numbers of a for lop:
num =7
for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break
        