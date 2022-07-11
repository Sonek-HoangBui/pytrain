
import math

a = float(input("Nhap a: "))

b = float(input("Nhap b: "))

if a.is_integer() and b.is_integer() and a > 0 and b > 0:
    print("a với b là 2 số nguyên dương")
else:
    print("Yêu cầu nhập a và b là số nguyên dương")
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    
c = a + b 
print("Tong là: ", c)
d = a - b 
print("Hieu là: ", d)
e = a / b 
print("Thuong là: ", e)
f = a * b 
print("Tich là: ", f)
g = a % b 
print(g) 

A = [c,d,e,f,g]
B = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(len(A)):
    for j in range(len(B)):
        print(A[i] ** B[j])

       
    
      




