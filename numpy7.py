#ตอนที่ 9 - ชนิดข้อมูล (Data Type)

import numpy as np


arr1 = np.array([1,2,3,4,5,6,7])
#แสดงอาเรย์
print(arr1.dtype)

#กำหนดเป็น type int
arr1 = np.array([1,2,3,4,5,6,7],dtype="int")
#แสดงอาเรย์
print(arr1)
print(arr1.dtype)

#กำหนดเป็น type float
arr1 = np.array([1,2,3,4,5,6,7],dtype="float")
#แสดงอาเรย์
print(arr1)
print(arr1.dtype)

#กำหนดเป็น type complex (จำนวนเชิงซ้อน)
arr1 = np.array([1,2,3,4,5,6,7],dtype="complex")
#แสดงอาเรย์
print(arr1)
print(arr1.dtype)

#หรือจะกำหนดเเบบ 2 มิติ
arr2 = np.array([[1,2],[3,4],[5,6]],dtype="float")
#แสดงอาเรย์
print(arr2)