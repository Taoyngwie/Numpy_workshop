#ตอนที่ 25 - Reshape & Resize

import numpy as np
#(reshape = row,columns)
arr1 = np.arange(1,11)
print(arr1)
b= arr1.reshape((2,5))
print(arr1.reshape((2,5)))
print(b)

# resize คือเปลี่ยนขนาดเเบบถาวร
arr1.resize((2,5))
print(arr1)