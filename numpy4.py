#ตอนที่ 6 - การเข้าถึงสมาชิก Array 1 มิติ (Index)

import numpy as np

#การสร้างเเบบ 1 มิติ
arr1 = np.array([1,2,3,4,5])
#แสดงอาเรย์
print(arr1)
#แสดงมิติ
print(arr1.ndim)

#เข้าถึงในแต่ละ index
    #แสดงเลข 3
print(arr1[2])
print(arr1[-3])


print(arr1[4])

print(arr1[3]+arr1[4])

#กำหนดค่าเป็นค่าอื่นในอาเรย์
arr1[2] = 100
print(arr1[2])