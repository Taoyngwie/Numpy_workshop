# ตอนที่ 17 - Arange

import numpy as np

# arr1 = np.arange(start,stop,step,dtype=..)

#สร้าง 0- 9 ออกมา
arr1 = np.arange(10)
print(arr1)

#สร้าง 1- 10 ออกมา
arr1 = np.arange(1,11,1)
print(arr1)

#สร้าง 1- 10 ออกมา(type float)
arr1 = np.arange(1,11,1,dtype="float")
print(arr1)

#สร้าง 1- 10 ออกมา(type complex)
arr1 = np.arange(1,11,1,dtype="complex")
print(arr1)


#สร้าง 1- 10 ออกมา(type int) เพิ่มทีละ 2
arr1 = np.arange(1,11,2)
print(arr1)
