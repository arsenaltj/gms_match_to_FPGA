
import numpy as np
mat1 = np.zeros((10, 10))
print(mat1)
f = open('out.txt', 'w')
for line in list(mat1):
    print(str(line).replace('.', '')[1:-2], file=f)

f.close()
