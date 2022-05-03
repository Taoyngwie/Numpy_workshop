#ตอนที่ 7 - การเข้าถึงสมาชิก Array 2 มิติ (Index)

from traceback import print_tb
import numpy as np

#การสร้างเเบบ 3 มิติ
arr3 = np.array([[[1,2,3],[4,5,6]]])
#แสดงอาเรย์
print(arr3)
#แสดงมิติ
print(arr3.ndim)

#การเข้าถึงภายใน
    #เข้าถึงเลข 5
print(arr3[0][1][1])
    #เข้าถึงเลข 3
print(arr3[0][0][2])

#อีกตัวอย่าง
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#แสดงอาเรย์
print(arr)

#การเข้าถึงภายใน
    #เข้าถึงเลข 8
print(arr[1][0][1])
    #เข้าถึงเลข 3
print(arr[0][0][2])

