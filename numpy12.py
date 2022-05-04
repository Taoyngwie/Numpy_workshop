#ตอนที่ 15 - Identity

import numpy as np

#Identity จะเป็นเเบบเเมทริกซ์จัสตุรัส
#สร้างอาเรย์ รูปเเบบเมตริกซ์เอกลักษณ์
# 1 มิติ
arr1 = np.identity(10) #ค่าเริ่มต้นเป็น float
print(arr1)

# 1 มิติ
arr1 = np.identity(10,dtype="int") #ค่าเริ่มต้นเป็น int
print(arr1)

#eye จะเป็นเมทริกซ์เอกลักษณ์ที่สามารถกำหนดขนาดได้
# 1 มิติ
arr1 = np.eye(3,4) #ค่าเริ่มต้นเป็น int
print(arr1)

# 1 มิติ
arr1 = np.eye(5) #ค่าเริ่มต้นเป็น int
print(arr1)

# 1 มิต(สามารถย้ายเลข 1 ได้)
    #ค่าบวกบ้ายขึ้น ค่าลบย้ายลง
arr1 = np.eye(5,k=1) #ค่าเริ่มต้นเป็น int
print(arr1)