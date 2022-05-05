#ตอนที่ 31 - Append & Insert


import numpy as np

a = np.array([[1,2],[3,4]])
np.append(a,10)

#inset ใส่ index ได้
print(np.insert(a,(1,2),10))