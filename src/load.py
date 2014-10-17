import numpy as np
import time
a = np.arange(65536)
a.reshape((256,256))
b = a
for i in range(1,1000000):
	b = a*a
	print(0.5/i)
	time.sleep(0.5/i)
