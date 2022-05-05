#ตอนที่ 22 - Index Operator

import numpy as np

# แบบ 1 มิติ
#เข้าถึงสมาชิกโดยใช้งาน Slice
arr1 = np.arange(1,11)

#นำมาสร้างโดยใช้งาน index จากอาเรย์ตัวเดิม
arindex = np.array([1,5,7])
print(arindex)

#เเสดงตำเเหน่งจากอาเรย์เดิม
print(arr1[arindex])


arindex = np.array([2,4,6,8])
#เเสดงตำเเหน่งจากอาเรย์เดิม
print(arr1[arindex])

# แบบ 2 มิติ
arrB = np.array([[1,2,3],[4,5,6],[7,8,9]])

#เอาเเถว 0 คอลัมน์ที่ 2 มาใช้งาน
print(arrB[[0,2]]) 

#เลือกมา 2 ตัว
print(arrB[[0,2],[2,0]])
#เลือกมา 2 ตัว
print(arrB[[0,2],[1]])