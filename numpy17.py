#ตอนที่ 19 - NumPy Attribute

import numpy as np

#ใช้งานเพื่อบอกโครงสร้างอาเรย์ว่ามีลักษณะอย่างไร

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="float")

#แสดงมิติ
print(arr1.ndim)
print(arr2.ndim)

#แสดงชนิดข้อมูล
print(arr1.dtype)
print(arr2.dtype)

#บอกรูปร่างของ อาเรย์
print(arr1.shape)
print(arr2.shape)

#แสดงจำนวนสมาชิก
print(arr1.size)
print(arr2.size)

#บอกขนาดของอาเรย์
print(arr1.itemsize)
print(arr2.itemsize)