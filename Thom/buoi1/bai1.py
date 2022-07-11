def nhaphoten():
    return input('Nhap ho va ten: ')
def string2list(hoten:str):  
    raw_list=hoten.split(" ")
    hoten_list=[]
    for item in raw_list:
       if item !='':
           hoten_list.append(item.casefold().capitalize())
    return hoten_list
def chuanhoa(hoten_list:list):
    hoten_str=''
    for item in hoten_list: 
         hoten_str +=item +" "
    hoten_str= hoten_str[: len(hoten_str)-1]
    print ("chuoi da chuan hoa: "+ hoten_str)