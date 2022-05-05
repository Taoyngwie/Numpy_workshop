#ตอนที่ 33 - ลบสมาชิกใน Array


import numpy as np

#แบบ 1 มิติ
arr1 = np.arange(1,21)
print(
np.split(arr1,4))

#แบบ 2 มิติ
arr1 = np.arange(1,21)
arr1 = arr1.reshape(5,4) 
print(arr1)
#แบ่งแนวตั้ง
print(np.hsplit(arr1,4))
#แบ่งแนวนอน
print(np.vsplit(arr1,5))