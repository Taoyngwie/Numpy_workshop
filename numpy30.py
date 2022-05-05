#ตอนที่ 32 - การ Insert Array 2 มิติ


import numpy as np

a1 = np.array([[12,22],[23,24]])
print(np.insert(a1,1,100,axis=0))

print(np.insert(a1,0,20,axis=1))