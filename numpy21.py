#ตอนที่ 23 - ตัวดำเนินการทางคณิตศาสตร์

import numpy as np

a = np.arange(1,6)

print(a)
#นำสมาชิกทุกตัวในอาเรย์ มาดำเนินการ กับ 2
print(a+2) 
print(a-2) 
print(a*2) 
print(a/2) 

#สามารถนำ 2 อาเรย์มา บวกกันได้
b = np.arange(1,7)
print(a+b)