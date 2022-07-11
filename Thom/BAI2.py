a=float(input("Nhap so a: "))
b=float(input("Nhap so b: "))
if(a.is_integer() and b.is_integer() and a>0 and b>0) : 
    print("a,b  là 2 so nguyen duong")
    c=a+b 
    print ( "tổng:" , c)
    d= a-b 
    print ("hieu:", d) 
    t= a*b
    print("tich: ",t)
    f=a/b 
    print("thuong:", f)
    
else:
    print("yeu cầu nhập a và b là số nguyên dương")
