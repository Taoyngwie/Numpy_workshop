#ตอนที่ 33 - ลบสมาชิกใน Array


import numpy as np
ar1 = np.array([5,8,78,13,4,6,86])
ar2 = np.array([[12,22],[23,24]])

#ลบใน 1 มิติ
print(np.delete(ar1,3))

#ลบเเถวที่ 2 ในเเนวนอน
print(np.delete(ar2,1,axis=0))

#ลบเเถวที่ 2 ในเเนวตั้ง
print(np.delete(ar2,1,axis=1))



