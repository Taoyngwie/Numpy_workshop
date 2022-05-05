#ตอนที่ 24 - Broadcasting

import numpy as np
#ไว้ใช้ ดำเนินการ ระหว่างอาเรย์โดยที่ มีขนาดไม่เท่ากัน
#โดยที่จะทำซ้ำในอาเรย์ที่มีขนาดเล็กกว่าขณะนำไปดำเนินการ

x = np.array([[1,2],[3,4],[5,6],[7,8]])
y = np.array([1,2])
sum1 = np.broadcast(x + y)
print(np.broadcast(x + y))


