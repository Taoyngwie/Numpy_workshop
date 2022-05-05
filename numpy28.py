#ตอนที่ 30 - Concatenate

from traceback import print_tb
import numpy as np

#การรวม2 อาเรย์โดยใช้เมธอด Concatenate
a = np.array([[1,2],[3,4]])
b = np.array([[12,22],[23,24]])
c = np.concatenate((a,b))
print(c)

#สามารถนำมาเพิ่มค่าโดยใช้ method (append)
a=np.append(a,1000)
print(a)

#สามารถนำมาประยุกต์เพิ่มเเบบเเนวนอนได้
print(np.append(b,[[10],[20]],axis=1))