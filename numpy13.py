#ตอนที่ 16 - Linspace

import numpy as np

#สามารถระบุได้ว่าต้องการให้อยู่ในช่วงใด เเละมีตัวเลขอยู่กี่ตัว

arr1 = np.linspace(1,10)
print(arr1)

arr1 = np.linspace(1,5)
print(arr1)

arr1 = np.linspace(1,5,4)
print(arr1)

#ไม่เอาตัวสุดท้าย
arr1 = np.linspace(1,5,endpoint=False)
print(arr1)