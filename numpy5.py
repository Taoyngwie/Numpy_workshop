#ตอนที่ 7 - การเข้าถึงสมาชิก Array 2 มิติ (Index)

import numpy as np

#การสร้างเเบบ 2 มิติ
arr2 = np.array([[1,2],[3,4],[5,6]])
#แสดงอาเรย์
print(arr2)
#แสดงมิติ
print(arr2.ndim)

#การเข้าถึงสมาชิกใน array
#เข้าถึงเลข 4
print(arr2[1][1])

#เข้าถึงเลข 5
print(arr2[2][0])
print(arr2[-1][-2])

#กำหนดค่าภายใน array 
arr2[1][0] = 500
print(arr2)

