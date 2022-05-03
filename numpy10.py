#ตอนที่ 13 - Matrix ค่าคงที่ (Full)

import numpy as np

#สร้างเมตริกซ์ ค่าคงที่ตามที่เรากำหนดไว้

# 1 มิติ
arr1 = np.full(5,10)
            #ช่องเเรก ขนาดมิติเเละจำนวนที่จะใส่ ช่องสอง เลขที่จำใส่ลงไปใน
print(arr1)

arr1 = np.full(7,15)
print(arr1)

#หรือจะใส่เป็นเลขทศนิยม
arr1 = np.full(7,5.3)
print(arr1)


# 2 มิติ
arr1 = np.full((3,3),7)
print(arr1)

# 3 มิติ
arr1 = np.full(((3,2,4)),1)
print(arr1)