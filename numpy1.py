#ตอนที่ 3 - การสร้าง Array 1 มิติ

import numpy as np

#การสร้างเเบบที่ 1
arr = np.array([1,2,3,4])
#แสดงอาเรย์
print(arr)
#แสดงมิติ
print(arr.ndim)


#สร้างอาเรย์เเบบที่ 2
l1 = [1,2,3,4]
ar2 = np.array(l1)

#แสดงอาเรย์
print(ar2)

#หรือจะสร้างแบบ tuple
tu = (1,2,3,4,5,6,7)
ar3 = np.array(tu)

#แสดงอาเรย๋์
print(ar3)