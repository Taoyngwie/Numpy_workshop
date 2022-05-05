#ตอนที่ 28 - Array และค่าทางสถิติ

import numpy as np

#ใช้กับอาเรย์ 1 มิติ
ar1 = np.array([5,8,78,13,4,6,86])
print(ar1.sum())
print(ar1.prod())
print(ar1.max())
print(ar1.min())
print(ar1.argmax())
print(ar1.argmin())

print()

#ใช้กับอาเรย์ 2 มิติ 
#axis 1 = เเนนนอน , 0 = เเนวตั้ง 
ar1 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(ar1.sum())
print(np.min(ar1,axis=1))
print(np.min(ar1,axis=0))










