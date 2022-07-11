def chuanhoaTen(str):
    string=''
    for word in str:
        string+=word.capitalize()+' '
    print(string)

def CheckIntegerPlus(a,b):
    while (a<0 or b<0) or (a.is_integer()== False or b.is_integer()==False):
        print("Yêu cầu nhập a và b là số nguyên dương")
        a=(input("nhap a: "))
        b=(input("nhap b: "))  
    if a.is_integer()== True and b.is_integer()==True:  
        print("Tổng: ",a+b)
        print("Hiệu: ",a-b)
        print("Tích: ",a*b)
        if b!=0:
            print("Thương: ",a/b)
        print("a %9: ",a%9)
        print("b %9: ",b%9)
        for i in range(1, 21):
            print("Mũ của a từ 1->20:", i ,pow(a,i))
        for i in range(1, 21):
            print("Mũ của b từ 1->20:", i ,pow(b,i))
        
#Chuẩn hóa tên 
x=(input("nhap: "))
str=x.split()
# str=x.capitalize()
chuanhoaTen(str)

# Kiểm tra số nguyên dương
a=float(input("nhap: "))
b=float(input("nhap: "))       
CheckIntegerPlus(a,b)

